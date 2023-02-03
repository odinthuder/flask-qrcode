from fastapi import FastAPI
from .api.qr import qr_route

app = FastAPI()

app.include_router(qr_route)