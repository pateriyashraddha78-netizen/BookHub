from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database import get_db
from ..models import Favorite
router=APIRouter()
class FavoriteIn(BaseModel): book_id:str;title:str;author:str="Unknown";cover_url:str=""
@router.get("")
def list_favorites(db:Session=Depends(get_db)): return db.query(Favorite).order_by(Favorite.created_at.desc()).all()
@router.post("")
def add_favorite(item:FavoriteIn,db:Session=Depends(get_db)):
 if db.query(Favorite).filter_by(book_id=item.book_id).first(): return {"message":"Already in favorites"}
 f=Favorite(**item.model_dump());db.add(f);db.commit();db.refresh(f);return f
@router.delete("/{book_id}")
def remove_favorite(book_id:str,db:Session=Depends(get_db)):
 f=db.query(Favorite).filter_by(book_id=book_id).first()
 if not f: raise HTTPException(404,"Favorite not found")
 db.delete(f);db.commit();return {"message":"Removed"}