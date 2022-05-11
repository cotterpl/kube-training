import logging
import os
from math import sqrt
from typing import Dict

import redis
from fastapi import FastAPI, HTTPException

logging.basicConfig(level=logging.INFO)

var_from_pod_definition = os.environ.get('VAR_FROM_POD_DEFINITION', '<NOT PROVIDED>')
var_from_config_map = os.environ.get('VAR_FROM_CONFIG_MAP', '<NOT PROVIDED>')
var_from_secret = os.environ.get('VAR_FROM_SECRET', '<NOT PROVIDED>')

database = None


def get_db() -> redis.Redis:
    global database
    if database is None:
        redis_host = os.environ.get('REDIS_HOST', None)
        if redis_host is None:
            raise HTTPException(status_code=500, detail='Redis connection is not configured')
        database = redis.Redis(
            host=redis_host,
            port=os.environ.get('REDIS_PORT', 6379),
            password=os.environ.get('REDIS_PASSWORD', None),
            db=os.environ.get('REDIS_DATABASE', 0),
        )
    return database


app = FastAPI()


@app.get("/")
async def hello() -> Dict:
    logging.info('Hello World called')
    return {"message": "Hello World"}


@app.get("/alive")
async def liveness_probe() -> Dict:
    logging.info('Liveness probe called')
    return {"message": "I am alive"}


@app.get("/ready")
async def readiness_probe(connections_check: bool = False) -> Dict:
    # you can check for example DB connection here
    logging.info('Readiness probe called')
    if (connections_check):
        get_db().ping()
        return {"message": "I am ready and connected"}
    return {"message": "I am ready"}


@app.get("/config")
async def get_config() -> Dict:
    logging.info('Asked for config')
    return {
        'VAR_FROM_POD_DEFINITION': var_from_pod_definition,
        'VAR_FROM_CONFIG_MAP': var_from_config_map,
        'VAR_FROM_SECRET': var_from_secret,
    }


@app.get("/hpatest")
async def hpa_test() -> Dict:
    x = 0.001
    for i in range(0, 50000):
        x += sqrt(x)
    return {'computed': x}


@app.get("/guests")
async def get_last_guest() -> Dict:
    last_guest = get_db().get('last_guest')
    return {'guest': last_guest}


@app.post("/guests")
async def set_last_guest(guest: str) -> Dict:
    get_db().set('last_guest', guest)
    return {'status': 'ok'}
