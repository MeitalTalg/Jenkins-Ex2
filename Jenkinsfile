pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python libraries...'
                    sh 'echo "jenkins" | sudo -S apt update'
                    sh 'echo "jenkins" | sudo -S apt install python3 pytest python3-pip'
                }
            }
        }
    }
}
