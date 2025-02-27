 
provider "kubernetes" {
  config_path = "~/.kube/config"  # Path to Minikube's kubeconfig
}

# Create a Kubernetes namespace
resource "kubernetes_namespace" "my_namespace" {
  metadata {
    name = "test-namespace"
  }
}

# Deploy a simple Nginx pod inside that namespace
resource "kubernetes_pod" "nginx_pod" {
  metadata {
    name      = "nginx"
    namespace = kubernetes_namespace.my_namespace.metadata[0].name
  }

  spec {
    container {
      image = "nginx:latest"
      name  = "nginx-container"
    }
  }
}