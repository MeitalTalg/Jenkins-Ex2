pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python libraries...'
                    sh 'echo "jenkins" | sudo -S apt update'
                    sh 'echo "jenkins" | sudo -S apt install -y python3 python3-pip'
                    sh 'echo "jenkins" | sudo -S pip install pytest'
                }
            }
        }
    }
}
