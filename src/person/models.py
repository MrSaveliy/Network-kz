
from sqlalchemy import  ForeignKey, Table, MetaData, Column, Integer, String, Date, Text
from database import Base

metadata = MetaData()

class Person(Base):
    __tablename__ = "person", 
    metadata,
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False)
    description = Column(String, unique=False)
    photo = Column(String, unique=False)
    clan = Column(String, unique=False)
    

person = Table (
    "person", 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
    Column("photo", String),
    Column("clan", String),
)    

assets = Table (
    "assets", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, unique=False),
    Column("description", String, unique=False),
    Column("photo", String, unique=False),
    Column("person_id", Integer, ForeignKey('person.id'), unique=False),
    
)
article = Table (
    "article", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String, unique=False),
    Column("subtitle", String, unique=False),
    Column("url", String, unique=False),
    Column("date", String, unique=False),
    Column("text", Text, unique=False),
    Column("sourse", String, unique=False) ,
    Column("person_id", Integer, ForeignKey('person.id'), unique=False),
    Column("assets_id", Integer, ForeignKey('assets.id'), unique=False),
 )

test_article = Table (
    "test_article", 
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String, unique=False),
    Column("subtitle", String, unique=False),
    Column("url", String, unique=False),
    Column("date", String, unique=False),
    Column("text", Text, unique=False),
    Column("sourse", String, unique=False) ,
    Column("person_id", Integer, ForeignKey('person.id'), unique=False),
    Column("assets_id", Integer, ForeignKey('assets.id'), unique=False),
 )