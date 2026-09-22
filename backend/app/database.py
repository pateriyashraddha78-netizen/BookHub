import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
url=os.getenv("DATABASE_URL","sqlite:///./bookhub.db");connect_args={"check_same_thread":False} if url.startswith("sqlite") else {}
engine=create_engine(url,connect_args=connect_args);SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
class Base(DeclarativeBase): pass
def get_db():
 db=SessionLocal()
 try: yield db
 finally: db.close()