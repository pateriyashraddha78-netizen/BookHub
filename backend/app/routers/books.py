import httpx
from fastapi import APIRouter,HTTPException,Query
router=APIRouter()
@router.get("")
async def search_books(query:str=Query("",max_length=200),page:int=Query(1,ge=1),limit:int=Query(20,ge=1,le=40)):
 if not query.strip(): return {"numFound":0,"docs":[],"page":page,"limit":limit}
 try:
  async with httpx.AsyncClient(timeout=10) as c:
   r=await c.get("https://openlibrary.org/search.json",params={"q":query.strip(),"page":page,"limit":limit});r.raise_for_status();data=r.json()
  docs=[]
  for b in data.get("docs",[]):
   key=b.get("key","").split("/")[-1];cover=b.get("cover_i");docs.append({"id":key,"title":b.get("title","Untitled"),"authors":b.get("author_name",[])[:3],"year":b.get("first_publish_year"),"rating":b.get("ratings_average"),"cover":f"https://covers.openlibrary.org/b/id/{cover}-M.jpg" if cover else ""})
  return {"numFound":data.get("numFound",0),"docs":docs,"page":page,"limit":limit}
 except Exception as e: raise HTTPException(502,"Book service unavailable") from e
@router.get("/{book_id}")
async def book_details(book_id:str):
 try:
  async with httpx.AsyncClient(timeout=10) as c:
   r=await c.get(f"https://openlibrary.org/works/{book_id}.json");r.raise_for_status();d=r.json()
  desc=d.get("description","");desc=desc.get("value","") if isinstance(desc,dict) else desc
  return {"id":book_id,"title":d.get("title","Untitled"),"description":desc,"subjects":d.get("subjects",[])[:8],"cover":f"https://covers.openlibrary.org/b/id/{d['covers'][0]}-L.jpg" if d.get("covers") else ""}
 except Exception as e: raise HTTPException(404,"Book not found") from e