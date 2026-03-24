# Deployment Guide
## Introduction
This document provides a step-by-step guide on deploying the Autonomous Fencing Supply Chain Optimizer.

## Prerequisites
The following prerequisites are required for deployment:

* **Docker**: Installed and running on the deployment machine.
* **Docker Compose**: Installed and running on the deployment machine.
* **PostgreSQL**: Installed and running on the deployment machine.

## Deployment Steps
The deployment steps are as follows:

1. Clone the repository: `git clone https://github.com/username/fencing-wood-merchant-wholesalers-optimi.git`
2. Navigate to the repository directory: `cd fencing-wood-merchant-wholesalers-optimi`
3. Build the Docker images: `docker-compose build`
4. Start the containers: `docker-compose up -d`
5. Initialize the database: `docker-compose exec db psql -U postgres -d optimi -f init.sql`
6. Access the web application: `http://localhost:8080`

## Environment Variables
The following environment variables are required for deployment:

* **POSTGRES_USER**: The PostgreSQL username.
* **POSTGRES_PASSWORD**: The PostgreSQL password.
* **POSTGRES_DB**: The PostgreSQL database name.
* **OPTIMI_API_KEY**: The API key for the optimization service.

## Monitoring and Logging
The system uses Prometheus and Grafana for monitoring and logging. The Prometheus configuration file is located at `prometheus.yml`, and the Grafana dashboard is available at `http://localhost:3000`.
