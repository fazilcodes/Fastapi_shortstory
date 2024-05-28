from fastapi import FastAPI
from routers.characters import router as characters_router
from routers.generate import router as generate_router

app = FastAPI()

app.include_router(characters_router)
app.include_router(generate_router)
