node{
    withEnv(['PATH+EXTRA=/usr/local/bin']) {
        stage('Get Plex Claim Token') {
            withCredentials([
                conjurSecretCredential(credentialsId:'plex_password',variable:'PLEX_PASSWORD'),
                conjurSecretCredential(credentialsId:'plex_username',variable:'PLEX_USERNAME')
                ]){
                sh'echo $PLEX_PASSWORD > newfile'
                sh'docker run -t --rm -e PLEX_USERNAME=$PLEX_USERNAME -e PLEX_PASSWORD=$PLEX_PASSWORD test > token || exit 0'
            }
        }
        stage('Update Docker Compose File') {
            def hostIP = InetAddress.localHost.hostAddress
            echo "${hostIP}"
            sh'sed -i "s/.*PLEX_CLAIM.*/      - PLEX_CLAIM=claim-$(cat token)/" docker-compose.yml'
            sh"sed -i 's/.*ADVERTISE_IP.*/      - ADVERTISE_IP=http:\\/\\/${hostIP}:32400\\//' docker-compose.yml"
        }
        stage('Launch Plex'){
                sh'docker pull plexinc/pms-docker'
                sh'docker rm plex -f'
                sh'docker-compose up -d' 
        }
    }
}