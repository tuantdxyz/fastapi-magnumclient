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
print(magnum.cluster_templates.list())
# cluster = magnum.clusters.list()[0]
# cluster_template = magnum.cluster_templates.list()[0]