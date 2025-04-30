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




## 🚀 Project Summary

This project showcases the deployment of a secure, containerised **Flask web application** to **Azure App Service**, using **Docker** and **Azure DevOps Pipelines** for CI/CD. The goal was to demonstrate a complete DevOps workflow—covering containerisation, automated deployment and Azure services.

---

## 🛠️ Tools & Technologies

- **Azure App Service** – Hosts the containerised application  
- **Azure Container Registry (ACR)** – Stores Docker images  
- **Azure Application Insights** – Enables observability and monitoring  
- **Docker** – Containerisation of the Flask app  
- **Azure DevOps Pipelines** – Automates build and deployment processes  
- **VS Code** – Local development environment  
- **GitHub** – Source code repository and pipeline integration  

---

## 🧱 Key Features

### ✅ Flask Application
- Simple Python web app returning `"Hello, World"` with Azure trace integration
![Screenshot 2025-04-30 154733](https://github.com/user-attachments/assets/e989cfe7-849a-454b-b4f0-d952ea9964fb)

### ✅ Containerisation
- `Dockerfile` used to package the Flask app into a portable container  
- Local testing via Docker Desktop
![Screenshot 2025-04-30 154759](https://github.com/user-attachments/assets/799fa74a-7614-4a81-a121-55332ccbece9)


### ✅ CI/CD Pipeline (Azure DevOps)
- `azure-pipelines.yml` defines pipeline steps:
  - Build Docker image
  - Push image to Azure Container Registry (ACR)
  - Deploy container to Azure App Service
![Screenshot 2025-04-30 152229](https://github.com/user-attachments/assets/02c73069-812b-4c66-af43-95fad08b3b25)
![Screenshot 2025-04-30 151650](https://github.com/user-attachments/assets/1da71b86-86f7-4464-b0dc-b8c4a8c93980)


### ✅ Monitoring with Application Insights
- Traces, requests, and performance metrics tracked using:
  ```python
  from opencensus.ext.azure.trace_exporter import AzureExporter
  from opencensus.ext.flask.flask_middleware import FlaskMiddleware
![Screenshot 2025-04-30 151239](https://github.com/user-attachments/assets/2ce7794b-22ef-4d87-8192-7c4c49e12ef1)
![Screenshot 2025-04-30 150837](https://github.com/user-attachments/assets/27b5ba8b-9b02-4abf-97d9-858c91521e62)

---

## ✅ Final Summary

This project demonstrates my ability to deliver a complete end-to-end DevOps solution using Microsoft Azure. From containerising the application with Docker, to automating deployments with Azure DevOps Pipelines, and setting up live monitoring using Application Insights—I gained practical, hands-on experience with key DevOps principles.

It reflects my capability in cloud-native tooling, infrastructure automation, and application observability critical skills for modern DevOps and Platform Engineering.

