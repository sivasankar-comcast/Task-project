pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 --version
                    pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                sh 'pytest test_main.py -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t task-api:latest .'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Starting app and checking health...'
                sh '''
                    docker run -d --name task-api-test -p 8001:8000 task-api:latest
                    sleep 5
                    curl http://localhost:8001/health
                    docker stop task-api-test
                    docker rm task-api-test
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline passed! All stages completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed! Copy the log above and paste into CI/CD Log Analyzer.'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}