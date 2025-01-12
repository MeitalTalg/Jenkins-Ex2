pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python libraries...'
                    sh 'echo "jenkins" | sudo -S apt update'
                    sh 'echo "jenkins" | sudo -S apt install -y python3 python3-pip python3-pytest'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'pytest tests'
                    
                }
            }
        }
        stage('Deploy') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            steps {
                script {
                    echo 'Deploying application...'
                    echo "Application deployed successfully!"
                }
            }
        }
        }
    }
}
