# *dawgif*

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

## 📌 Pipeline Flow Chart

![Pipeline Flow Chart](https://github.com/user-attachments/assets/9107e140-0309-4867-b2f5-cb2e27fc2196)


---

## ⚙️ CI/CD Pipeline Flow  

This project uses **GitHub Actions** to automate testing, building, and deployment. Below is the step-by-step flow of the CI/CD pipeline:  

### 1️⃣ Code Push & CI/CD Trigger  
- A push to the `main` branch or a pull request triggers the pipeline.  

### 2️⃣ Checkout Repository  
- The workflow pulls the latest code from the repository.  

### 3️⃣ Install Terraform  
- Downloads and installs **Terraform** for infrastructure management.  

### 4️⃣ Set Up Python Environment  
- Installs Python and dependencies from `requirements.txt`.  

### 5️⃣ Run Tests  
- Executes unit tests to ensure the application is working correctly.  

### 6️⃣ Authenticate with Google Cloud  
- Uses a **service account key** to log in to Google Cloud and set the correct project.  

### 7️⃣ Install GKE Auth Plugin & kubectl  
- Installs tools required to interact with **Google Kubernetes Engine (GKE)**.  

### 8️⃣ Get GKE Cluster Credentials  
- Retrieves Kubernetes credentials to deploy the application.  

### 9️⃣ Initialize & Apply Terraform  
- Provisions the GKE cluster using **Terraform**.  

### 1️⃣0️⃣ Generate Version Tag  
- Creates a **new version tag** based on the number of commits in the repository.  

### 1️⃣1️⃣ Build & Push Docker Image  
- **Builds a Docker image** and pushes it to **Google Artifact Registry (GAR)**.  

### 1️⃣2️⃣ Deploy to Kubernetes  
- Updates the Kubernetes deployment with the new image and **restarts pods** to apply changes.  

---

The pipeline ensures **automated, secure, and efficient** deployment of the Flask-based **Dawgif** app.

---

## 🛠️ Tech Stack  

- **Flask** – Web framework  
- **Docker** – Containerization  
- **GitHub Actions** – CI/CD automation  
- **Terraform** – Infrastructure provisioning  
- **Google Artifact Registry** – Image storage  
- **Google Kubernetes Engine (GKE)** – Kubernetes hosting  
