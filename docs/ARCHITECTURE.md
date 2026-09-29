# Architecture

The KeyHelp sidebar opens a same-origin manager iframe. A per-installation token is sent to the manager and included in API POST requests. The CGI validates request method, content type, same-origin origin and token, then delegates only allow-listed operations to root-owned helper scripts through sudoers rules. Status collectors write JSON consumed by the manager UI.
