import os
import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "service": "sre-demo",
        "version": os.getenv("APP_VERSION", "dev"),
        "pod": socket.gethostname(),
    }


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    return {"status": "ready"}
