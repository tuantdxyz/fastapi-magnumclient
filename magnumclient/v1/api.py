# -*- coding: utf-8 -*-
from fastapi import FastAPI
from magnumclient.v1.auth import AuthSingleton
import uvicorn
from magnumclient.v1.controller import cluster_controller, cluster_templates_controller
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.responses import UJSONResponse, Response

app = FastAPI()
# cors
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# router
prefix = '/api/v1'
app.include_router(cluster_controller.router, prefix=prefix, tags=['cluster'])
app.include_router(cluster_templates_controller.router, prefix=prefix, tags=['cluster_templates'])

# magnum server
magnum = AuthSingleton()

# test api
@app.get("/ping")
async def read_item():
    # my_str = "hello world, dân trí"
    # cfg = ("apiVersion: v1\n"
    #        "clusters:\n"
    #        "- cluster:\n"
    #        "    server: %(api_address)s\n"
    #        "  name: %(name)s\n"
    #        "contexts:\n"
    #        "- context:\n"
    #        "    cluster: %(name)s\n"
    #        "    user: %(name)s\n"
    #        "  name: %(name)s\n"
    #        "current-context: %(name)s\n"
    #        "kind: Config\n"
    #        "preferences: {}\n"
    #        "users:\n"
    #        "- name: %(name)s'\n"
    #        % {'name': "tuan", 'api_address': "hn"})
    #
    # my_str_as_bytes = str.encode(cfg)
    # response = Response(content=my_str_as_bytes, media_type='text/plain')
    return {"ping": "pong"}
    # return response


# Run api
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
# uvicorn magnumclient.v1.api:app --host 0.0.0.0 --port 8000
