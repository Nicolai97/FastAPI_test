from fastapi import FastAPI
from app.core.database import init_db
from app.routers import prodotto

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(prodotto.router)
