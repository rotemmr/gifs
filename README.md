#dawgif

Dawgif is a **Flask-based** web application that dynamically serves a random dog GIF. The app is **containerized with Docker**, deployed on **Google Kubernetes Engine (GKE)**, and managed through **Terraform**. The **CI/CD pipeline** is automated using **GitHub Actions**, and the container images are stored in **Google Artifact Registry**

---

## 🚀 Features

- **Flask Web Application** serving random dog GIFs  
- **GitHub Actions CI/CD** for automated testing & deployment  
- **Dockerized Deployment** for easy portability  
- **Google Artifact Registry** for storing container images  
- **Infrastructure as Code (IaC)** with Terraform for GKE provisioning  
- **Kubernetes Deployment** for scalable and reliable hosting  

---

## 📌 Project Architecture Diagram

*(Insert an architecture diagram here if available)*  

---

## ⚙️ CI/CD Pipeline Flow  

### 1️⃣ Code Push & CI/CD Pipeline Trigger  
- A push to the repository triggers **GitHub Actions**, which initiates the pipeline.  

### 2️⃣ Building & Pushing Docker Image  
- The Flask app is containerized using **Docker** and pushed to **Google Artifact Registry**.  

### 3️⃣ Testing with Docker Compose  
- The application is tested locally to ensure stability before deployment.  

### 4️⃣ Infrastructure Provisioning with Terraform  
- A **GKE cluster** is provisioned using **Terraform**.  

### 5️⃣ Deployment to Kubernetes  
- The application is deployed to **GKE** using Kubernetes manifests.  

---

## 🛠️ Tech Stack  

- **Flask** – Web framework  
- **Docker** – Containerization  
- **GitHub Actions** – CI/CD automation  
- **Terraform** – Infrastructure provisioning  
- **Google Artifact Registry** – Image storage  
- **Google Kubernetes Engine (GKE)** – Kubernetes hosting  
