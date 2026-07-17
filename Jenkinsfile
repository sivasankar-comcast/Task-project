pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Setup Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    python3 --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'pytest test_main.py -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t task-api:latest .'
            }
        }
    }

    post {
        success {
            echo '✅ All stages passed!'
        }
        failure {
            echo '❌ Pipeline failed — copy this log into your CI/CD Analyzer!'
        }
    }
}