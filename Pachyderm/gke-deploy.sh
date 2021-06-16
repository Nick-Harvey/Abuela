CLUSTER_NAME="pach-cluster"

GCP_ZONE="us-east1-c"

gcloud config set compute/zone ${GCP_ZONE}

gcloud config set container/cluster ${CLUSTER_NAME}

MACHINE_TYPE="n1-standard-4"

# By default the following command spins up a 3-node cluster. You can change the default with `--num-nodes VAL`.
gcloud container clusters create ${CLUSTER_NAME} --scopes storage-rw --machine-type ${MACHINE_TYPE}

# By default, GKE clusters have RBAC enabled. To allow 'pachctl deploy' to give the 'pachyderm' service account
# the requisite privileges via clusterrolebindings, you will need to grant *your user account* the privileges
# needed to create those clusterrolebindings.
#
# Note that this command is simple and concise, but gives your user account more privileges than necessary. See
# https://docs.pachyderm.io/en/latest/deployment/rbac.html for the complete list of privileges that the
# pachyderm serviceaccount needs.
kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value account)