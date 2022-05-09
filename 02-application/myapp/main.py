import logging

from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)

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