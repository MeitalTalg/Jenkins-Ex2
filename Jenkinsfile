pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python libraries...'
                    sh 'echo "jenkins" | sudo -S apt update'
                    sh 'sudo apt install -y python3 pytest python3-pip'
                }
            }
        }
    }
}
