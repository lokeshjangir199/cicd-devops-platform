from fastapi import FastAPI

app = FastAPI(title="CI/CD DevOps Platform")


@app.get("/")
def root():
    return {
        "message": "CI/CD DevOps Platform is running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }
