# Cloud Deployment Lab

## Project Overview

This project demonstrates how to develop a Python Flask web application, containerize it using Docker, store the source code on GitHub, and deploy it on an AWS EC2 instance.

The application displays a welcome message, the student's name, and the application version.

## Technologies Used

- Python
- Flask
- Gunicorn
- Docker
- Git and GitHub
- AWS EC2

## Project Structure

```text
cloud-deployment-lab/
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Run Locally with Docker

### 1. Build the image

```bash
docker build -t cloud-deployment-lab:1.0 .
```

### 2. Run the container

```bash
docker run -d --name cloud-lab -p 5000:5000 cloud-deployment-lab:1.0
```

### 3. Test the application

Open `http://localhost:5000` in a browser.

Health endpoint: `http://localhost:5000/health`

### 4. Check the container

```bash
docker ps
docker logs cloud-lab
```

## AWS EC2 Deployment

1. Launch an EC2 Linux instance.
2. Configure its security group to allow SSH from your IP address and TCP port 5000 for the web application.
3. Connect to the instance using SSH.
4. Install and start Docker.
5. Clone this repository.
6. Build the Docker image.
7. Run the container with port mapping `5000:5000`.
8. Open `http://EC2_PUBLIC_IP:5000` in a browser.

## Deployment Verification

- Local application: `http://localhost:5000`
- EC2 application: `http://EC2_PUBLIC_IP:5000`
- Health endpoint: `/health`
- Container status: `docker ps`

Replace `EC2_PUBLIC_IP` with the instance's actual public IPv4 address.

## Troubleshooting

Document the actual errors encountered and their resolutions here. For example:

- **Container exits:** Check logs using `docker logs cloud-lab`.
- **Application is unreachable:** Verify the container is running, port mapping is correct, and the EC2 security group allows TCP port 5000.
- **Git push fails:** Check the remote repository URL and GitHub authentication.

## Conclusion

This lab demonstrates the complete workflow of developing, version-controlling, containerizing, and deploying a web application on AWS EC2.

## Student Details

- Name: YOUR NAME
- Repository: https://github.com/YOUR_USERNAME/cloud-deployment-lab
- Application version: 1.0.0
