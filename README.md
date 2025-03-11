# *dawgif*

Dawgif is a **Flask-based** web application that dynamically serves a random dog pics. The app is **containerized with Docker**, deployed on **Google Kubernetes Engine (GKE)** with **Helm**, and managed through **Terraform**. The **CI/CD pipeline** is automated using **GitHub Actions**, and the container images are stored in **Google Artifact Registry**

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

![Pipeline Flow Chart](https://github.com/user-attachments/assets/db658874-c13f-4643-9e97-eab480e01a12)

---

## CI/CD Pipeline Workflow

### 1️⃣ **Code Push & CI/CD Trigger**

- ✔️ The workflow is triggered by pushes and pull requests to the `main` branch.

### 2️⃣ **Checkout Code**

- ✔️ The `actions/checkout@v2` action is used to pull the latest code from the repository.

### 3️⃣ **Set Up Python Environment**

- ✔️ Python 3.9 is set up using `actions/setup-python@v2`.
- ✔️ Dependencies are installed from `requirements.txt` using `pip install`.

### 4️⃣ **Generate Version Tag**

- ✔️ The workflow generates a unique version tag based on the commit count.
- ✔️ The version tag is pushed back to the repository to ensure consistency in deployment.
- ✨ **Improvement**: `::set-output` is deprecated, so the version info is now stored in the environment using `echo "VERSION=$VERSION" >> $GITHUB_ENV`.

### 5️⃣ **Build & Push Docker Image**

- ✔️ The Docker image is built using the generated version tag and pushed to the Google Artifact Registry.
- ✨ **Consideration**: You can add `docker-compose` or `docker buildx` for multi-platform builds if necessary.

### 6️⃣ **Run Unit Tests**

- ✔️ Unit tests are run using the `unittest discover` command to ensure the application works as expected.

### 7️⃣ **Authenticate with Google Cloud**

- ✔️ The Google Cloud Service Account key (`GCP_SA_KEY`) is securely used for authentication.
- ✔️ The key is saved in a temporary file, and `gcloud auth` is used for authentication.

### 8️⃣ **Install Helm**

- ✔️ Helm is downloaded and installed to manage Kubernetes deployments.

### 9️⃣ **Install Terraform**

- ✔️ Terraform is installed to manage infrastructure provisioning on Google Cloud.

### 🔟 **Add GCP GPG Key**

- ✔️ The GPG key is added to the system to install packages from Google Cloud.

### 1️⃣1️⃣ **Install GKE Auth Plugin & kubectl**

- ✔️ The GKE authentication plugin and `kubectl` are installed for managing Kubernetes clusters.

### 1️⃣2️⃣ **Get GKE Cluster Credentials**

- ✔️ The workflow configures `kubectl` with the correct GKE cluster credentials to allow for deployments to the Kubernetes cluster.

### 1️⃣3️⃣ **Initialize Terraform**

- ✔️ Terraform is initialized in the `terraform-gke` directory, preparing it to manage the Google Cloud infrastructure.

### 1️⃣4️⃣ **Apply Terraform**

- ✔️ Terraform `apply` is executed to provision or update the infrastructure on Google Cloud.

### 1️⃣5️⃣ **Deploy to Kubernetes with Helm**

- ✔️ The latest Docker image is deployed to the Kubernetes cluster using Helm.
- ✔️ `kubectl get pods -o wide` is used to confirm that the Kubernetes deployment was successfully updated.

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
- **Helm** - Easier deploying with kubernetes  
