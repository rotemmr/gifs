variable "GCP_SA_KEY" {
  type        = string
  description = "Google Cloud Service Account Key"
}

provider "google" {
  credentials = jsondecode(var.GCP_SA_KEY)
  project     = "devops-451510"
  region      = "us-central1"
}

data "google_client_config" "default" {}

data "google_container_cluster" "primary" {
  name     = "flask-cluster"
  location = "us-central1-a"
}

provider "kubernetes" {
  host                   = "https://${data.google_container_cluster.primary.endpoint}"
  cluster_ca_certificate = base64decode(data.google_container_cluster.primary.master_auth[0].cluster_ca_certificate)
  token                  = data.google_client_config.default.access_token
}

# Update deployment name to match the existing one
resource "kubernetes_deployment" "flask_app" {
  metadata {
    name      = "flask-app-deployment"  # Use the correct deployment name
    namespace = "default"
    labels = {
      app = "flask-app"
    }
  }

  spec {
    replicas = 3  # Adjust as needed

    selector {
      match_labels = {
        app = "flask-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "flask-app"
        }
      }

      spec {
        container {
          name  = "flask-container"
          image = "us-central1-docker.pkg.dev/devops-451510/my-docker-repo/project-flask-app:latest"
          port {
            container_port = 5000
          }
          resources {
            limits = {
              cpu    = "500m"
              memory = "512Mi"
            }
            requests = {
              cpu    = "250m"
              memory = "256Mi"
            }
          }
        }
      }
    }
  }
}

output "cluster_endpoint" {
  value = data.google_container_cluster.primary.endpoint
}

output "cluster_ca_certificate" {
  value = data.google_container_cluster.primary.master_auth[0].cluster_ca_certificate
}

output "access_token" {
  value     = data.google_client_config.default.access_token
  sensitive = true
}

