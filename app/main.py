from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import router as web_router

app = FastAPI(title="Follow Balance")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(web_router)
