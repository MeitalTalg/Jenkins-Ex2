pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python libraries...'
                    echo env.SHELL
                    sh 'sudo apt update'
                    sh 'sudo apt install -y python3 pytest python3-pip'
                }
            }
        }
    }
}
