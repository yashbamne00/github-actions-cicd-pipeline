\# AWS EC2 Docker Web Application Deployment



\## About



This project shows how to deploy a Flask web application on an AWS EC2 Ubuntu server using Docker, Docker Compose, and Nginx.



\## Technologies



\- AWS EC2

\- Ubuntu 22.04

\- Docker

\- Docker Compose

\- Flask

\- Nginx

\- Linux

\- SSH



\## Project Structure



```

aws-docker-deployment/

│── app.py

│── requirements.txt

│── Dockerfile

│── docker-compose.yml

│── README.md

└── screenshots/

```



\## How to Run



\### Build Docker Image



```bash

docker build -t flask-app .

```



\### Run Docker Container



```bash

docker run -d -p 5000:5000 flask-app

```



\### Run with Docker Compose



```bash

docker-compose up -d

```



\## Output



Open your browser and visit:



```

http://EC2\_PUBLIC\_IP

```



You should see:



```

Hello from AWS Docker!

```



\## Screenshots



The `screenshots` folder contains:



\- AWS EC2 Instance

\- Docker Installation

\- Running Docker Container

\- Browser Output



\## What I Learned



\- Launching an AWS EC2 instance

\- Connecting with SSH

\- Installing Docker and Docker Compose

\- Creating Docker images

\- Running Docker containers

\- Configuring Nginx as a reverse proxy

\- Deploying a Flask application on AWS

