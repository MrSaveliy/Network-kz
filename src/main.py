from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from person.router import router as router_person
from pages.router import router as router_pages

app = FastAPI(
    title="Network"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router_pages)
app.include_router(router_person)