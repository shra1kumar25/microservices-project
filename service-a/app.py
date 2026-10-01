from fastapi import FastAPI, HTTPException
from client import get_product, get_user
from client import get_service_data

app = FastAPI()

@app.get("/")
def home():
    return {"service": "Order Service"}

@app.get("/health")
def health():
    return {
        "service": "order-service",
        "status": "healthy"
    }


@app.get("/order")
def get_order():

    product = requests.get(
        "http://localhost:8002",
         timeout=5
    ).json()

    user = requests.get(
        "http://localhost:8003"
    ).json()

    return {
        "order_id": 5001,
        "customer": user,
        "product": product
    }

@app.get("/invoice")
def get_invoice():

    try:
        product = get_product()
        user = get_user()

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Backend service unavailable: {str(e)}"
        )

    price = product["price"]

    tax = price * 0.18

    total = price + tax

    return {
        "invoice_id": 9001,
        "customer_name": user["name"],
        "product_name": product["product_name"],
        "price": price,
        "tax": tax,
        "total": total
    }
