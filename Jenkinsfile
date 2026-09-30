pipeline {
    agent any

    environment {
        IMAGE_NAME = "customer-portal"
        CONTAINER_NAME = "customer-portal-test"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-jenkins',
                    url: 'https://github.com/ajayvarada6/customer-portal.git'
            }
        }

        stage('Build') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:build-%BUILD_NUMBER% .'
            }
        }

        stage('Container Verification') {
            steps {
                bat 'docker run -d --name %CONTAINER_NAME% -p 8081:8080 %IMAGE_NAME%:build-%BUILD_NUMBER%'
                bat 'timeout /t 5'
                bat 'curl http://localhost:8081/health'
            }
        }

        stage('Cleanup') {
            steps {
                bat 'docker stop %CONTAINER_NAME%'
                bat 'docker rm %CONTAINER_NAME%'
            }
        }
    }
}