# CI Pipeline Demo

This project demonstrates a complete CI/CD pipeline using GitHub Actions, including automated testing, Docker containerization, and deployment.

## Features

- GitHub Actions workflow for CI/CD
- Automated testing with pytest
- Docker containerization
- Automated deployment pipeline

## Setup

1. Clone the repository
2. Create the following secrets in your GitHub repository:
   - `DOCKER_HUB_USERNAME`: Your Docker Hub username
   - `DOCKER_HUB_TOKEN`: Your Docker Hub access token

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn app.main:app --reload
```

3. Run tests:
```bash
pytest tests/
```

## Docker

Build the image:
```bash
docker build -t api-test .
```

Run the container:
```bash
docker run -p 8000:8000 api-test
```

## CI/CD Pipeline

The CI/CD pipeline consists of three main stages:

1. **Test**: Runs automated tests using pytest
2. **Build and Push**: Builds Docker image and pushes to Docker Hub
3. **Deploy**: Handles deployment (customize based on your deployment target)

The pipeline is triggered on:
- Push to main branch
- Pull requests to main branch
