from fastapi import FastAPI

app = FastAPI(title="JP-Delivery-Marketplace", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Welcome to JP-Delivery-Marketplace!"}