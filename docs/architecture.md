# Project 2 - CI/CD Architecture

## Architecture Diagram

```text
Developer
    |
    | Git Push
    v
GitHub Repository
    |
    | Webhook Trigger
    v
Jenkins CI/CD Pipeline
    |
    | Checkout Source Code
    v
Docker Build
    |
    | Push Docker Image
    v
AWS Elastic Container Registry (ECR)
    |
    | Pull Latest Image through SSH
    v
AWS EC2 Instance
    |
    v
Docker Container
    |
    v
Flask Application
    |
    v
Nginx Reverse Proxy
    |
    v
User Accesses Application
