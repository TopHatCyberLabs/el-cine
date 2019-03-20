# el-cine

Deletes old Plex container and launches a new one after pulling the latest pms-docker container

## requirements

- Uses CyberArk Conjur and Jenkins integration for secrets management. If you do not have Conjur, you can use regular Jenkins secrets, but you'll need to change the secrets declaration.
- Jenkins is installed on the same host as Docker. Will not work in a Jenkins container as written.
- Pyhton 3.7 installed on the host in /usr/src/bin