
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-flask-app .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker rm -f flask-app || true
                    docker run -d -p 5000:5000 --name flask-app jenkins-flask-app
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
                echo 'Application deployment completed!'
            }
        }
    }
}
