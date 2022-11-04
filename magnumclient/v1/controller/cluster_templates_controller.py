# -*- coding: utf-8 -*-
from fastapi import APIRouter
from magnumclient.v1.auth import AuthSingleton

router = APIRouter()
magnum = AuthSingleton()


@router.get("/cluster_templates")
async def get_cluster_templates():
    cluster_templates = magnum.cluster_templates.list()
    result = [obj.to_dict() for obj in cluster_templates]
    res = {"data": result, "size": len(cluster_templates)}
    return res


@router.get("/cluster_templates/{_id}")
async def get_cluster_templates_by_id(_id: str):
    cluster_templates = magnum.cluster_templates.get(_id)
    result = cluster_templates.to_dict()
    res = {"data": result}
    return res
