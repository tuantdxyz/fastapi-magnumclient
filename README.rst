========================
Magnumclient v3.0.1
========================
REQUIREMENTS

* python3.9

SETUP and RUN

* pip3 install -r requirements.txt
* export PBR_VERSION=1.2.3
* python3 setup.py install
* uvicorn magnumclient.v1.api:app --host 0.0.0.0 --port 8000 (or run api.py)
* api: http://localhost:8000/docs

Architecture Magnum API
=================================

![image](https://user-images.githubusercontent.com/74556484/199879828-24812e6b-aeab-41c6-99e9-fd948b3b5731.png)

