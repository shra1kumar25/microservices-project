from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_user():

    return {
        "user_id": 1,
        "name": "Sravan",
        "city": "Hyderabad"
    }

@app.get("/health")
def health():
    return {
        "service": "user-service",
        "status": "healthy"
    }
