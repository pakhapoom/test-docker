# Test Docker Application

This project demonstrates a simple Dockerized application with a FastAPI-based frontend and backend.

## Prerequisites

- Docker
- Docker Compose

## Setup and Deployment

1. **Clone the Repository**
```zsh
git clone https://github.com/pakhapoom/test-docker.git
cd test-docker
```

2. **Start the Services**
```zsh
docker compose up
```
Please note that 
- The frontend will be available at [http://localhost:5000](http://localhost:5000).
- The backend will be available at [http://localhost:5001](http://localhost:5001).

3. **Access the Application**
- Open a browser and navigate to [http://localhost:5000](http://localhost:5000).
- Enter a username in the form and submit it.
- The backend will respond with a greeting message displayed on the frontend.
