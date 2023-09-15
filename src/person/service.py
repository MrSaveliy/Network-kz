from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from person import models, schemas

## PERSON
# async def create_person(session: AsyncSession, person: schemas.PersonCreate):
#     stmt = insert(models.person).values(**person.dict())
#     await session.execute(stmt)
#     await session.commit()
#     query = select(models.person).where(models.person.c.id == person.id)
#     results = await session.execute(query)
#     return {"status": "success",
#             "person": results.mappings().fetchall()}

async def get_all_persons(session: AsyncSession):
    query = select(models.person)  
    results = await session.execute(query)
    persons = results.mappings().fetchall()  
    return persons

async def get_person_by_name(session: AsyncSession, name: str):
    query = select(models.person).where(models.person.c.name == name)  
    results = await session.execute(query)
    man = results.mappings().fetchall()  
    return man

## ARTICLES
# async def create_article(session: AsyncSession, article: schemas.ArticleCreate):
#     stmt = insert(models.article).values(**article.dict())
#     await session.execute(stmt)
#     await session.commit()
#     query = select(models.article).where(models.article.c.id == article.id)
#     results = await session.execute(query)
#     return {"status": "success",
#             "person": results.mappings().fetchall() }

async def get_articles_by_sourse(session: AsyncSession, sourse: str):
    query = select(models.article).where(models.article.c.sourse == sourse)  
    results = await session.execute(query)
    articles = results.mappings().fetchall()  
    return articles

async def get_articles_by_date(session: AsyncSession, dates: str):
    query = select(models.article).where(models.article.c.date == dates)  
    results = await session.execute(query)
    articles = results.mappings().fetchall()  
    return articles

async def get_articles_by_person_name(session: AsyncSession, person_name: str):
    query = select(models.person).where(models.person.c.name == person_name)  
    results = await session.execute(query)
    id = results.mappings().fetchall()[0]["id"]
    query_1 = select(models.article).where(models.article.c.person_id == id)
    results_1 = await session.execute(query_1)
    articles = results_1.mappings().fetchall()  
    return articles


async def parse_article(session: AsyncSession, article: dict):
    stmt = insert(models.article).values(article)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


## ASSETS