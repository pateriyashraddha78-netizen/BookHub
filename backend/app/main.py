from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base,engine
from .routers import books,favorites,history
Base.metadata.create_all(bind=engine)
app=FastAPI(title="BookHub API",version="1.0.0",description="Book discovery and personal library API")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
@app.get("/health")
def health(): return {"status":"ok"}
app.include_router(books.router,prefix="/books",tags=["books"]);app.include_router(favorites.router,prefix="/favorites",tags=["favorites"]);app.include_router(history.router,prefix="/history",tags=["history"])