from fastapi import Request
from fastapi.responses import HTMLResponse
from gardener import app, templates, BASE_DIR
from .models.models import Item



@app.get("/")
def init():
    print(BASE_DIR)
    return {"Hello": BASE_DIR}


@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
