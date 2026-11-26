# Automated CI/CD Pipeline using Jenkins, Docker and AWS

## Project Overview

This project demonstrates an automated CI/CD pipeline for deploying a Python Flask application using Jenkins, Docker and AWS.

Whenever code changes are pushed to GitHub, a GitHub Webhook automatically triggers Jenkins.

Jenkins builds the Docker image, pushes it to Amazon ECR, deploys the updated container to an Amazon EC2 instance and verifies the deployment.

## Technologies Used

- AWS EC2
- AWS Elastic Container Registry (ECR)
- Jenkins
- Docker
- Git and GitHub
- GitHub Webhooks
- Python
- Flask
- Linux
- Nginx
- Shell Scripting

## CI/CD Pipeline Stages

1. GitHub: Developer pushes code changes.
2. Webhook: GitHub automatically triggers Jenkins.
3. Checkout: Jenkins retrieves source code.
4. Build: Jenkins builds the Docker image.
5. Push: Docker image is pushed to AWS ECR.
6. Deploy: Jenkins connects to EC2 using SSH and deploys the latest image.
7. Verify: Jenkins uses curl to verify application availability.

## Architecture

Developer
    |
    v
GitHub Repository
    |
    v
GitHub Webhook
    |
    v
Jenkins Pipeline
    |
    v
Docker Image Build
    |
    v
AWS ECR
    |
    v
AWS EC2
    |
    v
Docker Container (Flask)
    |
    v
Nginx Reverse Proxy
    |
    v
Live Application

## Project Structure

jenkins-docker-cicd/
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
└── .gitignore

## Jenkins Credentials

- aws-credentials: AWS authentication.
- ec2-ssh-key: EC2 SSH authentication.

Credentials are managed through Jenkins Credentials.

## Deployment Verification

Application response:

HTTP/1.1 200 OK

Version 3: Successfully deployed through automated Jenkins CI/CD Pipeline!

Jenkins Build Status:

Finished: SUCCESS

## Key Learnings

- Automated CI/CD pipeline implementation.
- GitHub Webhook integration with Jenkins.
- Docker image creation and management.
- AWS ECR integration.
- Automated deployment to AWS EC2.
- SSH-based remote deployment.
- Application deployment verification.

## Author

Gokila D.

GitHub: https://github.com/GokilaD123
