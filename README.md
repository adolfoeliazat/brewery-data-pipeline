# Brewery Data Pipeline

## Overview
This project is a data pipeline that fetches data from the Open Brewery DB API, processes it through the Medallion architecture (Bronze, Silver, and Gold layers), and orchestrates tasks using Apache Airflow. The data is transformed and stored in a structured format.

## Requirements
- Docker
- Docker Compose

## Setup

1. **Build the Docker Container**
   ```bash
   docker build -t brewery-pipeline .
