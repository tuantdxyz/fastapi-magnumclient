# -*- coding: utf-8 -*-
from keystoneauth1.identity import v3
from keystoneauth1 import session
from magnumclient.client import Client


class AuthSingleton(object):
    magnum = None
    magnum_endpoint = "http://172.16.1.76:9511/v1"

    auth = v3.Password(auth_url='http://172.16.1.6:5000/v3',
                       username='admin',
                       password='36329bc73c274fba',
                       project_name='admin',
                       user_domain_id='default',
                       project_domain_id='default')
    sess = session.Session(auth=auth)

    magnum = Client('1', endpoint_override=magnum_endpoint, session=sess)

    def __new__(cls):
        if not cls.magnum:
            print("disconnect magnum server")
        return cls.magnum


# obj = AuthSingleton()
# print(obj.clusters.list())