from pydantic import BaseModel
from typing import Union, List


class Cluster(BaseModel):
    uuid: str
    name: str
    cluster_template_id: str
    keypair: str
    node_count: int
    master_count: int
    docker_volume_size: int
    status: str
    health_status: Union[str, None] = None

    class Config:
        orm_mode = True


class ClusterIn(BaseModel):
    uuid: Union[str, None] = None
    name: Union[str, None] = None
    cluster_template_id: Union[str, None] = None
    node_count: int
    master_count: Union[int, None] = None
    keypair: Union[str, None] = None
    nodes_to_remove: Union[List[str], None] = None
    # master_flavor_id: str
    # flavor_id: str
    # create_timeout: Union[int, None] = None
    # docker_volume_size: Union[int, None] = None
    # labels: Labels

    class Config:
        orm_mode = True

    # def to_dict(self, **kwargs):
    #     result = dict()
    #     ignore_fields = kwargs or []
    #     print("TTT")
    #
    #     for key in ignore_fields:
    #         if key in ignore_fields:
    #             continue
    #         val = getattr(self, key, None)
    #         # if isinstance(val, DatabaseModel):
    #         #     result[key] = val.to_dict(None)
    #         # elif isinstance(val, enum.Enum):
    #         #     result[key] = val.value
    #         # elif isinstance(val, datetime.datetime):
    #         #     result[key] = val.strftime('%Y-%m-%d %H:%M')
    #         # else:
    #         result[key] = val
    #     return result


# class Item(BaseModel):
#     name: str
#     description: str