from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from person.router import get_person_by_name, get_articles_by_person_name

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/search_person/{name}")
def get_search_page(request: Request, persons=Depends(get_person_by_name)):
    return templates.TemplateResponse("search_person.html", {"request": request, "person": persons})

@router.get("/search_articles/{person_name}")
def get_search_articles_by_person_name(request: Request, articles=Depends(get_articles_by_person_name)):
    return templates.TemplateResponse("search_articles.html", {"request": request, "articles": articles})