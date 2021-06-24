CLUSTER_NAME=dev-t4-cluster
POOL_NAME=gpu-t4
GPU_TYPE=nvidia-tesla-t4
GCP_ZONE=us-east1-c
GCP_REGION=us-east1
AMOUNT=1
MACHINE_TYPE=n1-standard-4
STORAGE_SIZE=30
BUCKET_NAME=pachyderm-gke-t4-dev
GCP_ZONE2=us-east1-d


gcloud config set compute/zone ${GCP_ZONE}

gcloud config set container/cluster ${CLUSTER_NAME}


# By default the following command spins up a 3-node cluster. You can change the default with `--num-nodes VAL`.
gcloud container clusters create ${CLUSTER_NAME} \
--accelerator type=${GPU_TYPE},count=${AMOUNT} \
--scopes storage-rw --machine-type ${MACHINE_TYPE} \
--region ${GCP_REGION} --node-locations ${GCP_ZONE}

# By default, GKE clusters have RBAC enabled. To allow 'pachctl deploy' to give the 'pachyderm' service account
# the requisite privileges via clusterrolebindings, you will need to grant *your user account* the privileges
# needed to create those clusterrolebindings.


# Note that this command is simple and concise, but gives your user account more privileges than necessary. See
# https://docs.pachyderm.io/en/latest/deployment/rbac.html for the complete list of privileges that the
# pachyderm serviceaccount needs.
kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value account)

echo "Installing Pachyderm"

pachctl deploy google ${BUCKET_NAME} ${STORAGE_SIZE} --dynamic-etcd-nodes=1