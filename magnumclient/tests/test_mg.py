from keystoneauth1.identity import v3
from keystoneauth1 import session
from magnumclient.client import Client
from magnumclient.common import utils as magnum_utils

magnum_endpoint = "http://172.16.1.76:9511/v1"

auth = v3.Password(auth_url='http://172.16.1.6:5000/v3',
                   username='admin',
                   password='36329bc73c274fba',
                   project_name='admin',
                   user_domain_id='default',
                   project_domain_id='default')
sess = session.Session(auth=auth)

magnum = Client('1', endpoint_override=magnum_endpoint, session=sess)
# list
print(magnum.clusters.list())
# print(magnum.cluster_templates.list())
# cluster = magnum.clusters.list()[0]
# cluster_template = magnum.cluster_templates.list()[0]

# download file config cluster
print(magnum_utils.config_cluster("tuan-kubernetes-02", "k8s-cluster", './'))
# print(magnum_utils.config_cluster(cluster, cluster_template, './'))

# # create cluster
# bays = {
#    "name": "k8s-06",
#    # "discovery_url": None,
#    "master_count": 1,
#    "baymodel_id": "1696bee6-74f5-484b-9085-33c3df383103",
#    "node_count": 2,
#    "bay_create_timeout": 60
# }

cluster = {
   "name": "k8s-07",
   # "discovery_url":null,
   "master_count": 1,
   "cluster_template_id": "1696bee6-74f5-484b-9085-33c3df383103",
   "node_count": 2,
   "create_timeout": 60,
   "keypair": "tuantd_key",
   "master_flavor_id": "m1.small",
   # "labels": {
   #      "floating_ip_enabled": True,
   #      "master_lb_enabled": True
   # },
   "flavor_id": "m1.medium"
}
# magnum.bays.create(**bays)
# magnum.clusters.create(**cluster)
# print(magnum.certificates.get("3d293807-c787-442f-b0db-3ddb05bf3595"))


# download file config cluster
# certificate-authority-data: ca.pem
# client-certificate-data: cert.pem
# client-key-data: key.pem

# get certificate-authority-data: [get] /v1/certificates/{cluster_ident}
# http://172.16.1.76:9511/v1/certificates/3d293807-c787-442f-b0db-3ddb05bf3595

# get client-certificate-data: [post] /v1/certificates/
# input: generate_csr_and_key()

# delete cluster
# magnum.clusters.delete("3d293807-c787-442f-b0db-3ddb05bf3595")


# resize cluster
resize_node = {
    "node_count": 3,
    # "nodes_to_remove": ["e74c40e0-d825-11e2-a28f-0800200c9a66"],
    # "nodegroup":　"production_group"
}

magnum.clusters.resize(cluster_uuid="d5b6f865-a67e-44cc-8504-010120f6d734", node_count=4,
                       nodes_to_remove=[], nodegroup="default-worker")

magnum.clusters.resize(cluster_uuid="k8s-01", node_count=4,
                       nodes_to_remove=[], nodegroup="default-worker")
# magnum.certificates.get()
print("T")
