import datetime
from pydantic import BaseModel

class PersonCreate(BaseModel):
    id: int
    name: str
    description: str
    photo: str
    clan: str

class ArticleCreate(BaseModel):
   title: str
   subtitle: str
   url: str
   date: str
   text: str
   sourse: str
   person_id: int   
   assets_id: int
