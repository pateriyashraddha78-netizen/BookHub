from sqlalchemy import String,Text,DateTime,func
from sqlalchemy.orm import Mapped,mapped_column
from .database import Base
class Favorite(Base):
 __tablename__="favorites";id:Mapped[int]=mapped_column(primary_key=True);book_id:Mapped[str]=mapped_column(String(200),unique=True,index=True);title:Mapped[str]=mapped_column(String(500));author:Mapped[str]=mapped_column(String(500),default="Unknown");cover_url:Mapped[str]=mapped_column(String(1000),default="");created_at:Mapped[DateTime]=mapped_column(DateTime,server_default=func.now())
class SearchHistory(Base):
 __tablename__="search_history";id:Mapped[int]=mapped_column(primary_key=True);query:Mapped[str]=mapped_column(String(500),index=True);created_at:Mapped[DateTime]=mapped_column(DateTime,server_default=func.now())