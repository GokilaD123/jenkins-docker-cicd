pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        IMAGE_URI = '217522443919.dkr.ecr.us-east-1.amazonaws.com/jenkins-flask-app'
        ECR_REGISTRY = '217522443919.dkr.ecr.us-east-1.amazonaws.com'
        EC2_HOST = '3.91.170.34'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/GokilaD123/jenkins-docker-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t jenkins-flask-app .
                    docker tag jenkins-flask-app:latest "$IMAGE_URI:latest"
                '''
            }
        }

        stage('Push Image to ECR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'aws-credentials',
                    usernameVariable: 'AWS_ACCESS_KEY_ID',
                    passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                )]) {
                    sh '''
                        export AWS_DEFAULT_REGION="$AWS_REGION"
                        aws ecr get-login-password --region "$AWS_REGION" |
                            docker login --username AWS --password-stdin "$ECR_REGISTRY"
                        docker push "$IMAGE_URI:latest"
                    '''
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                withCredentials([sshUserPrivateKey(
                    credentialsId: 'ec2-ssh-key',
                    keyFileVariable: 'SSH_KEY',
                    usernameVariable: 'SSH_USER'
                )]) {
                    sh '''
                        ssh -i "$SSH_KEY" \
                            -o StrictHostKeyChecking=no \
                            "$SSH_USER@$EC2_HOST" \
                            "sudo docker pull $IMAGE_URI:latest &&
                             (sudo docker rm -f flask-app || true) &&
                             sudo docker run -d --restart unless-stopped \
                             --name flask-app \
                             -p 127.0.0.1:5000:5000 \
                             $IMAGE_URI:latest"
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'curl -f http://$EC2_HOST/'
            }
        }
    }
}
