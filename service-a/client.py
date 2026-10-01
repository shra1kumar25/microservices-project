import os
import requests
from dotenv import load_dotenv

load_dotenv()

PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL"
)

USER_SERVICE_URL = os.getenv(
    "USER_SERVICE_URL"
)


def get_service_data(url):
    response = requests.get(
        url,
        timeout=5
    )

    response.raise_for_status()

    return response.json()


def get_product():
    return get_service_data(
        PRODUCT_SERVICE_URL
    )


def get_user():
    return get_service_data(
        USER_SERVICE_URL
    )
