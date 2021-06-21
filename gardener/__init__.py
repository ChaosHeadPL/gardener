import os
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .config import Settings


BASE_DIR = os.path.dirname(__file__)

app = FastAPI()

# mount static dir:
app.mount("/static",
          StaticFiles(directory=os.path.join(BASE_DIR, "static")),
          name="static")

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


config = Settings().dict()


from gardener.routes import *
