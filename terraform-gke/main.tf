provider "google" {
  credentials = file("/home/rotem1535/keys/service-acc.json")
  project     = "devops-451510"
  region      = "us-central1"
}

data "google_container_cluster" "primary" {
  name     = "flask-cluster"
  location = "us-central1-a"
}

provider "kubernetes" {
  host                   = data.google_container_cluster.primary.endpoint
  cluster_ca_certificate = base64decode(data.google_container_cluster.primary.master_auth[0].cluster_ca_certificate)
  token                  = data.google_container_cluster.primary.master_auth[0].access_token
}

