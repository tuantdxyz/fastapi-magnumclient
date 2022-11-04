# -*- coding: utf-8 -*-
from fastapi import APIRouter
from magnumclient.v1.auth import AuthSingleton
from magnumclient.v1.models.base_model import ResponseModel
from magnumclient.v1.models.cluster_model import Cluster, ClusterIn
from magnumclient.common import utils
from fastapi.responses import Response

router = APIRouter()
magnum = AuthSingleton()


@router.post("/cluster")
async def create_cluster(item: ClusterIn):
    clusters = magnum.clusters.create(**item.__dict__)
    result = clusters.to_dict()
    res = {"data": result}
    return res


@router.get("/cluster", response_model=ResponseModel)
async def get_clusters():
    clusters = magnum.clusters.list()
    # cluster_templates = magnum.cluster_templates.list()
    # item = ClusterTemplates(**clusters[0].to_dict())
    result = [Cluster(**obj.to_dict()) for obj in clusters]
    # result.sort(key=lambda obj: obj["uuid"])
    res = {"data": result, "size": len(clusters)}
    return res


@router.get("/cluster/{_id}")
async def get_cluster_by_id(_id: str):
    clusters = magnum.clusters.get(_id)
    result = clusters.to_dict()
    res = {"data": result}
    return res


@router.delete("/cluster/{_id}")
async def delete_cluster_by_id(_id: str):
    magnum.clusters.delete(_id)
    res = {"data": "OK"}
    return res


# resize node worker
@router.post("/cluster/resize")
async def resize_cluster(item: ClusterIn):
    clusters = magnum.clusters.resize(cluster_uuid=item.uuid, node_count=item.node_count)
    result = clusters.to_dict()
    res = {"data": result}
    return res


# file config
@router.get("/cluster/config/{_id}")
async def get_config_cluster(_id: str):
    clusters = magnum.clusters.get(_id)
    certificates_cluster = utils.generate_csr_and_key()
    certificates = {
        'cluster_uuid': clusters.uuid,
        'csr': certificates_cluster['csr']
    }
    ca_server = magnum.certificates.get(_id)
    ca_client = magnum.certificates.create(**certificates)
    certs = {
        'ca': ca_server.pem,
        'private_key': certificates_cluster['key'],
        'public_key': ca_client.pem
    }
    cfg_str = utils.config_cluster_kubernetes_magnum(clusters, certs)
    cfg_str_as_bytes = str.encode(cfg_str)
    response = Response(content=cfg_str_as_bytes, media_type='text/plain')
    return response
