main.py

from fastapi import FastAPI

app = FastAPI(title="Bail Response Integration API")


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Bail Response Integration API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
