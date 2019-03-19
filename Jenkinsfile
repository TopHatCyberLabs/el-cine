pipeline{
    agent any
    environment {
        PATH = "$PATH:/usr/local/bin"
    }
    stages{
        stage('Get Plex Claim Token') {
            environment{
                withCredentials([conjurSecretCredential(credentialsId: 'plex_password', variable: 'plex_password')])
            }
                steps{
                    sh'docker run -t --rm -e PLEX_USERNAME=mark.t.hurter@gmail.com -e PLEX_PASSWORD=$plex_password test > token || exit 0'
                    def token = sh(script:'cat token', returnStdout:true).trim()
                    if (token.length() == 0){
                        println 'Could not retrieve Plex Claim Token.'
                        currentBuild.result = 'FAILURE'
                    }
                    else{
                        sh'rm token -f'
                    }
                }
        }
        stage('Update Docker Compose File') {
            steps{
                def hostIP = InetAddress.localHost.hostAddress
                sh'sed -i "s/.*PLEX_CLAIM-.*/      - PLEX_CLAIM=claim-${token}/" docker-compose.yml'
                sh'sed -i "s/.*ADVERTISE_IP.*/      - ADVERTISE_IP=http:\\/\\/${hostIP}:32400\\//" docker-compose.yml'
             }
        }
        stage('Launch Plex'){
            steps{
                sh'docker pull plexinc/pms-docker'
                sh'docker rm plex -f'
                sh'docker-compose up -d' 
            }
        }
    }
}