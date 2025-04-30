# AZURE-CICD-APP-PROJECT

_(DevOps, CI/CD, Containerisation)_

## Architecture:
![Screenshot 2025-04-30 091944](https://github.com/user-attachments/assets/3029a5e8-66db-4fd5-98a0-fb80814ce5e3)


## Overview

This project demonstrates the deployment of a containerised Flask web application to Azure App Service using Azure DevOps for CI/CD. The pipeline builds and pushes a Docker image to Azure Container Registry, then automatically deploys it to Azure App Service.

## Tools Used:

- **Azure App Service** – Hosting the Flask app
- **Azure Container Registry (ACR)** – Storing Docker images
- **Azure DevOps Pipelines** – CI/CD automation
- **Docker** – Containerising the application
- **Flask** – Python web application framework
- **Azure Monitor & Application Insights** - Real time performance monitoring, logs, and alerts for the containerised app

## Pipeline Flow:

1. **Push code** to Azure Repos
2. **Build** Docker image in Azure DevOps
3. **Push** image to ACR
4. **Deploy** container to Azure App Service
5. **Monitor** performance and availability via Azure Monitor & Application Insights
