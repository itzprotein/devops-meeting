# DevOps Meeting Application

This repository contains a Flask-based web application for managing meetings and events. It's designed as a DevOps lab practice project for students to learn containerization and Kubernetes deployment.

## Project Overview

This is a web application built with Flask that provides various UI components and meeting management features. The application includes:

- User authentication (sign-in and sign-up)
- Event management (adding and viewing events)
- Schedule management
- Various UI components (avatars, alerts, badges, etc.)

## Technical Stack

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy
- **Frontend**: HTML/CSS/JavaScript (templates)

## Prerequisites

- Python 3.x
- Docker
- kubectl (for Kubernetes deployment)
- Access to a Kubernetes cluster

## Local Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Access the application at http://localhost:5000

## DevOps Lab Instructions

### Part 1: Containerization

Students are required to:

1. Create a Dockerfile for the application
2. Build a Docker image
3. Test the containerized application locally
4. Push the image to a container registry (Docker Hub, AWS ECR, etc.)

### Part 2: Kubernetes Deployment

Students are required to complete the following tasks:

#### Task 1: Deploy a Simple Web App on Kubernetes
1. Create Kubernetes deployment manifests (deployment.yaml, service.yaml)
2. Deploy the Flask application to a Kubernetes cluster
3. Expose it via a Service
4. Configure appropriate resources and scaling policies
5. Implement health checks and readiness probes

#### Task 2: Rolling Updates and Rollbacks
1. Deploy the application with version v1
2. Update it to v2 using kubectl set image
3. Perform a rollback if needed
4. Document the process and commands used

#### Task 3: Cluster-wide Load Balancing with Services
1. Deploy multiple instances of the application
2. Expose them via a LoadBalancer or NodePort service
3. Test and verify the load balancing functionality
4. Document the configuration and results

## Accessing the Kubernetes Cluster

For access to the Kubernetes cluster environment, please reach out to Engineer Idris. He will provide the necessary credentials and connection details.

## Submission Requirements

- Dockerfile
- Kubernetes manifest files
- Technical wiki page documenting your project
- Brief documentation of your deployment process
- Any issues encountered and how they were resolved

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [Flask Documentation](https://flask.palletsprojects.com/)

## Happy Learning DevOps Afritech!

This project is designed to give you hands-on experience with essential DevOps tools and practices. Don't hesitate to ask questions and collaborate with your peers.
