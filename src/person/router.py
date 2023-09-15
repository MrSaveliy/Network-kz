import time
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

from person import models, service
from person import schemas
from parser.kapitalkz import start_parser_kapitalkz
from parser.tengrinewskz import start_parser_tengrinewskz


router = APIRouter(
    prefix="/network",
    tags=["Network"]
)

# Person 
# @router.post("/add-person")
# async def create_person(person: schemas.PersonCreate, session: AsyncSession = Depends(get_async_session)):
#     try:
#         new_person =  await service.create_person(person=person, session=session)
#         return new_person
#     except HTTPException as ex:
#         print(ex)  

@router.get("/get-all-persons")
async def get_all_persons(session: AsyncSession = Depends(get_async_session)):
    try:
        all_person = await service.get_all_persons(session=session)
        return all_person
    except HTTPException as ex:
        print(ex)

@router.get("/get-person-by-name")
async def get_person_by_name(name: str, session: AsyncSession = Depends(get_async_session)):
    try:
        person = await service.get_person_by_name(name=name, session=session )
        return person[0]   
    except HTTPException as ex:
        print(ex)

# Article
# @router.post("/add-article")
# async def create_article(article: schemas.ArticleCreate, session: AsyncSession = Depends(get_async_session)):
#     try: 
#         new_article = await service.create_article(article=article, session=session)
#         return new_article
#     except HTTPException as ex:
#             print(ex)

@router.get("/get-articles-by-sourse")
async def get_articles_by_sourse(sourse: str, session: AsyncSession = Depends(get_async_session)):
    try:
        articles = await service.get_articles_by_sourse(session=session, sourse=sourse)
        return articles
    except HTTPException as ex:
        print(ex)

@router.get("/get-articles-by-date")
async def get_articles_by_date(dates: str, session: AsyncSession = Depends(get_async_session)):
    try:
        articles = await service.get_articles_by_date(session=session, dates=dates)
        return articles
    except HTTPException as ex:
        print(ex)

@router.get("/get-articles-by-person-name")
async def get_articles_by_person_name(person_name: str, session: AsyncSession = Depends(get_async_session)):
    try:
        articles = await service.get_articles_by_person_name(session=session,person_name=person_name)
        return articles
    except HTTPException as ex:
        print(ex)

@router.post("/parse-article")
async def parse_article(session: AsyncSession = Depends(get_async_session)):
    try:
        parse_list_kapitalkz = start_parser_kapitalkz()
        for article_kapitalkz in parse_list_kapitalkz:
            await service.parse_article(article=article_kapitalkz, session=session)
        parse_list_tengrinewsk = start_parser_tengrinewskz()
        for article_tengrinewsk in parse_list_tengrinewsk:
            await service.parse_article(article=article_tengrinewsk, session=session)    
        return {'message:' : "seccess"}    
    except HTTPException as ex:
            print(ex)

# Assets
