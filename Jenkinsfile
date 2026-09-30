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
                bat 'C:\\Users\\ajayv\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'C:\\Users\\ajayv\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'C:\\Users\\ajayv\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe build -t %IMAGE_NAME%:build-%BUILD_NUMBER% .'
            }
        }

        stage('Container Verification') {
            steps {
                bat 'C:\\Users\\ajayv\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe run -d --name %CONTAINER_NAME% -p 8081:8080 %IMAGE_NAME%:build-%BUILD_NUMBER%'
                bat 'timeout /t 5'
                bat 'curl http://localhost:8081/health'
            }
        }

        stage('Cleanup') {
            steps {
                 bat 'C:\\Users\\ajayv\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe stop %CONTAINER_NAME%'
                 bat 'C:\\Users\\ajayv\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe rm %CONTAINER_NAME%'
                
            }
        }
    }
}