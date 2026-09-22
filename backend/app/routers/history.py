from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database import get_db
from ..models import SearchHistory
router=APIRouter()
class SearchIn(BaseModel): query:str
@router.get("")
def list_history(db:Session=Depends(get_db)): return db.query(SearchHistory).order_by(SearchHistory.created_at.desc()).limit(20).all()
@router.post("")
def add_history(item:SearchIn,db:Session=Depends(get_db)):
 q=item.query.strip()
 if not q:return {"message":"Skipped"}
 last=db.query(SearchHistory).order_by(SearchHistory.created_at.desc()).first()
 if not last or last.query.lower()!=q.lower(): db.add(SearchHistory(query=q));db.commit()
 return {"message":"Saved"}
@router.delete("")
def clear_history(db:Session=Depends(get_db)): db.query(SearchHistory).delete();db.commit();return {"message":"Cleared"}