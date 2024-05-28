from fastapi import FastAPI
from routers.characters import router as characters_router
from routers.generate import router as generate_router

app = FastAPI()

app.include_router(characters_router)
app.include_router(generate_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)