import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "service": "sre-demo",
        "version": "v2",
        "pod": socket.gethostname(),
        "message": "rolling update complete"
    }


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    return {"status": "ready"}
