#!/usr/bin/env python3
import json,os,subprocess,sys,re,datetime
SECRET_FILE='/etc/keyhelp-docker-manager.secret'
with open(SECRET_FILE,'r',encoding='utf-8') as f:
 EXPECTED=f.read().strip()

AUDIT_LOG='/var/log/keyhelp-docker-manager-audit.log'
MAX_BODY=16384

def client_ip():
 return (
  os.environ.get('REMOTE_ADDR','-')
  .replace('\n',' ')
  .replace('\r',' ')
 )[:80]

def audit(action='-',target='-',result='-',detail=''):
 try:
  now=datetime.datetime.now(
   datetime.timezone.utc
  ).isoformat()

  safe_action=str(action).replace('\n',' ').replace('\r',' ')[:80]
  safe_target=str(target).replace('\n',' ').replace('\r',' ')[:180]
  safe_result=str(result).replace('\n',' ').replace('\r',' ')[:80]
  safe_detail=str(detail).replace('\n',' ').replace('\r',' ')[:500]

  with open(AUDIT_LOG,'a',encoding='utf-8') as f:
   f.write(
    f'{now} ip={client_ip()} '
    f'action={safe_action!r} '
    f'target={safe_target!r} '
    f'result={safe_result!r} '
    f'detail={safe_detail!r}\n'
   )
 except Exception:
  pass

def security_fail(message,code=403):
 audit(result='DENIED',detail=message)
 reply(False,message,code)
 raise SystemExit

def validate_origin():
 origin=os.environ.get('HTTP_ORIGIN','').strip()

 # Manche same-origin Requests senden keinen Origin-Header.
 if not origin:
  return

 host=os.environ.get('HTTP_HOST','').strip()
 scheme=os.environ.get('REQUEST_SCHEME','https').strip() or 'https'
 allowed={f'{scheme}://{host}'} if host else set()

 if origin not in allowed:
  security_fail('Anfrage von diesem Ursprung nicht erlaubt.',403)

def validate_request():
 if os.environ.get('REQUEST_METHOD','')!='POST':
  security_fail('Nur POST erlaubt.',405)

 content_type=(
  os.environ.get('CONTENT_TYPE','')
  .split(';',1)[0]
  .strip()
  .lower()
 )

 if content_type!='application/json':
  security_fail('Nur application/json erlaubt.',415)

 if os.environ.get('HTTP_X_REQUESTED_WITH','')!='KeyHelpDockerManager':
  security_fail('Ungültige Anfrage.',403)

 validate_origin()

 try:
  length=int(os.environ.get('CONTENT_LENGTH','0') or '0')
 except ValueError:
  security_fail('Ungültige Request-Länge.',400)

 if length < 2:
  security_fail('Leere Anfrage.',400)

 if length > MAX_BODY:
  security_fail('Anfrage zu groß.',413)

 return length

def reply(ok,out,code=0):
 print('Content-Type: application/json; charset=utf-8'); print('Cache-Control: no-store'); print(); print(json.dumps({'ok':ok,'code':code,'output':out},ensure_ascii=False))
try:
 n=validate_request()
 raw=sys.stdin.read(n)
 try:
  data=json.loads(raw)
 except json.JSONDecodeError:
  security_fail('Ungültiges JSON.',400)

 if not isinstance(data,dict):
  security_fail('JSON-Objekt erwartet.',400)
 action=str(data.get('action','')).strip()
 target=str(data.get('target','')).strip()

 if not action or len(action)>64:
  security_fail('Ungültige Aktion.',400)

 if len(target)>512:
  security_fail('Ungültiges Ziel.',400)
 if action not in {
    'start',
    'stop',
    'restart',
    'logs',
    'inspect',
    'remove-container',
    'backup',
    'update-check',
    'update',
    'install-engine',
    'docker-version',
    'pull-image',
    'remove-image',
        'volume-list',
    'volume-inspect',
    'volume-create',
'remove-volume',
    'prune-images',
    'prune-build-cache',
    'install-git',
    'compose-up',
    'docker-run',
    'project-start',
    'project-stop',
    'project-restart',
    'project-pull',
    'project-build',
    'project-deploy',
    'project-git-deploy',
    'project-logs',
    'project-config',
    'project-down',
    'registry-list',
    'registry-login',
    'registry-logout',
    'registry-test',
    'network-list',
    'network-inspect',
    'network-create',
    'network-remove',
    'network-connect',
    'network-disconnect',
}: reply(False,'Aktion nicht erlaubt.',400); raise SystemExit
 # Ziel abhängig von der Aktion validieren.
 # Container-/Volume-Namen und Image-Referenzen haben unterschiedliche Syntax.
 if target:
  if len(target)>512:
   reply(False,'Ziel ist zu lang.',400)
   raise SystemExit

  simple_target_actions={
   'start',
   'stop',
   'restart',
   'logs',
   'inspect',
   'remove-container',
   'update',
   'remove-volume',
     'volume-inspect',
   'volume-create',
}

  image_target_actions={
   'pull-image',
   'remove-image',
  }

  if action in simple_target_actions:
   if not all(c.isalnum() or c in '_.-' for c in target):
    reply(False,'Ungültiges Ziel.',400)
    raise SystemExit

  elif action in image_target_actions:
   # Zulässige Docker-Image-Referenzen:
   # nginx
   # nginx:latest
   # library/nginx:latest
   # ghcr.io/owner/image:tag
   # registry.example.de:5000/owner/image:tag
   allowed=set(
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '0123456789'
    '._-/:@'
   )

   if not target or any(c not in allowed for c in target):
    reply(False,'Ungültige Image-Referenz.',400)
    raise SystemExit
 project_actions={
  'install-git',
  'compose-up',
  'docker-run',
  'project-start',
  'project-stop',
  'project-restart',
  'project-pull',
  'project-build',
  'project-deploy',
  'project-git-deploy',
  'project-logs',
  'project-config',
  'project-down',
 }
 if action in project_actions:
  cmd=['sudo','/usr/local/sbin/ricorewi-docker-project-action',action]
  
 # REGISTRY_ACTION_MARKER_5C3B1
 if action.startswith('registry-'):
  registry=str(data.get('registry','')).strip()
  username=str(data.get('username','')).strip()

  if (
   registry and
   (
    len(registry)>253 or
    not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._:-]*',registry)
   )
  ):
   security_fail('Ungültige Registry.',400)

  registry_helper='/usr/local/sbin/ricorewi-docker-registry'

  if action=='registry-list':
   rcmd=['sudo',registry_helper,'list']
   password=None

  elif action=='registry-login':
   password=str(data.get('password',''))

   if not registry:
    security_fail('Registry fehlt.',400)

   if not username or len(username)>200:
    security_fail('Ungültiger Benutzername.',400)

   if not password or len(password)>4096:
    security_fail('Ungültiges Passwort oder Token.',400)

   rcmd=[
    'sudo',
    registry_helper,
    'login',
    registry,
    username
   ]

  elif action=='registry-logout':
   if not registry:
    security_fail('Registry fehlt.',400)

   password=None
   rcmd=[
    'sudo',
    registry_helper,
    'logout',
    registry
   ]

  elif action=='registry-test':
   if not registry:
    security_fail('Registry fehlt.',400)

   password=None
   rcmd=[
    'sudo',
    registry_helper,
    'test',
    registry
   ]

  else:
   security_fail('Registry-Aktion nicht erlaubt.',400)

  audit(action,registry,'REQUEST','registry')

  try:
   rp=subprocess.run(
    rcmd,
    input=(password+'\n') if password is not None else None,
    text=True,
    capture_output=True,
    timeout=120
   )

   rout=(rp.stdout+rp.stderr)[-12000:]

   # Docker login kann die Registry nennen,
   # aber wir protokollieren niemals rout/password.
   audit(
    action,
    registry,
    'OK' if rp.returncode==0 else 'ERROR',
    'exit='+str(rp.returncode)
   )

   reply(
    rp.returncode==0,
    rout,
    rp.returncode
   )

  except subprocess.TimeoutExpired:
   audit(action,registry,'TIMEOUT','registry timeout')
   reply(False,'Registry-Anfrage hat das Zeitlimit überschritten.',504)

  raise SystemExit

 if action not in project_actions:
  # NETWORK_ROUTING_MARKER_5C3C
  network_actions={
   'network-list',
   'network-inspect',
   'network-create',
   'network-remove',
   'network-connect',
   'network-disconnect',
  }
  if action in network_actions:
   cmd=['sudo','/usr/local/sbin/ricorewi-docker-network',action]
  else:
   cmd=['sudo','/usr/local/sbin/ricorewi-docker-action',action]+([target] if target else [])

 timeouts={
    'inspect':15,
    'logs':20,
    'docker-version':15,
    'start':60,
    'stop':60,
    'restart':90,
    'update-check':180,
    'update':600,
    'backup':600,
    'pull-image':600,
    'remove-container':60,
    'remove-image':60,
        'volume-list':60,
    'volume-inspect':60,
    'volume-create':60,
'remove-volume':60,
    'prune-images':180,
    'prune-build-cache':180,
    'install-engine':600,
    'install-git':2400,
    'compose-up':2400,
    'docker-run':900,
    'project-start':900,
    'project-stop':300,
    'project-restart':600,
    'project-pull':1800,
    'project-build':2400,
    'project-deploy':3600,
    'project-git-deploy':3600,
    'project-logs':90,
    'project-config':120,
    'project-down':600,
     'network-list':30,
     'network-inspect':30,
     'network-create':60,
     'network-remove':60,
     'network-connect':60,
     'network-disconnect':60,
}
 timeout=timeouts.get(action,60)

 try:
  p=subprocess.run(
      cmd,
      text=True,
      capture_output=True,
      input=(json.dumps(data) if action in project_actions or action in network_actions else None),
      timeout=timeout
  )
  combined=(p.stdout+p.stderr)[-30000:]

  audit(
      action,
      target,
      'OK' if p.returncode==0 else 'ERROR',
      'exit='+str(p.returncode)
  )

  reply(
      p.returncode==0,
      combined,
      p.returncode
  )
 except subprocess.TimeoutExpired as e:
  out=''
  if e.stdout:
   out += e.stdout if isinstance(e.stdout,str) else e.stdout.decode(errors='replace')
  if e.stderr:
   out += e.stderr if isinstance(e.stderr,str) else e.stderr.decode(errors='replace')
  audit(action,target,'TIMEOUT','timeout='+str(timeout))
  reply(False,'Zeitüberschreitung nach '+str(timeout)+' Sekunden.\n'+out[-10000:],504)
except Exception as e: reply(False,'Interner Fehler: '+str(e),500)
