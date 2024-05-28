from fastapi import FastAPI, Request
from routers.characters import router as characters_router
from routers.generate import router as generate_router
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", { "request": request })


app.include_router(characters_router)
app.include_router(generate_router)
