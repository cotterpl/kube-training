import logging
import os
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)

var_from_pod_definition = os.environ.get('VAR_FROM_POD_DEFINITION', '<NOT PROVIDED>')
var_from_config_map = os.environ.get('VAR_FROM_CONFIG_MAP', '<NOT PROVIDED>')
var_from_secret = os.environ.get('VAR_FROM_SECRET', '<NOT PROVIDED>')


app = FastAPI()


@app.get("/")
async def hello():
    logging.info('Hello World called')
    return {"message": "Hello World"}

@app.get("/alive")
async def liveness_probe():
    logging.info('Liveness probe called')
    return {"message": "I am alive"}

@app.get("/ready")
async def readiness_probe():
    # you can check for example DB connection here
    logging.info('Readiness probe called')
    return {"message": "I am ready"}

@app.get("/config")
async def get_config():
    logging.info('Asked for config')
    return {
        'VAR_FROM_POD_DEFINITION': var_from_pod_definition,
        'VAR_FROM_CONFIG_MAP': var_from_config_map,
        'VAR_FROM_SECRET': var_from_secret,
    }