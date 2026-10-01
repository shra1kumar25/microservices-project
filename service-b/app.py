from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_product():

    return {
        "product_id": 101,
        "product_name": "Laptop",
        "price": 50000
    }
@app.get("/health")
def health():
    return {
        "service": "product-service",
        "status": "healthy"
    }
