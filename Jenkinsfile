pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python libraries...'
                    echo $SHELL
                    sh 'sudo apt update'
                    sh 'apt install -y python3 pytest python3-pip'
                }
            }
        }
