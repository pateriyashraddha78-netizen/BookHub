# BookHub

BookHub is a full-stack book discovery and personal library application. It lets users search books, open detailed information, save favorites, and review or clear recent searches.

## Features

- Book search by title, author, or keyword
- Open Library API integration through FastAPI
- Responsive React + TypeScript interface
- Book details with cover, description, and subjects
- Persistent favorites using SQLAlchemy
- Persistent search history
- React Query caching and mutations
- Loading, empty, and error states
- Light/dark theme toggle with persistence
- FastAPI health endpoint
- Render deployment configuration

## Tech Stack

**Frontend:** React, TypeScript, Vite, Tailwind CSS, React Router, TanStack React Query, Sonner

**Backend:** Python, FastAPI, SQLAlchemy, SQLite locally / PostgreSQL-compatible configuration

## Local Setup

### Backend

```bash
cd backend
python -m venv venv
# Windows
venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Copy `backend/.env.example` to `.env` when custom configuration is needed.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Copy `.env.example` to `.env` and set:

```env
VITE_API_URL=http://localhost:8000
```

Frontend: http://localhost:5173  
API docs: http://localhost:8000/docs  
Health: http://localhost:8000/health

## Deployment

The repository includes `render.yaml` for a separate FastAPI web service and frontend static site. Set the frontend `VITE_API_URL` to the deployed backend URL in Render.

## Project Structure

```
frontend/
  src/
    App.tsx
    main.tsx
    index.css
backend/
  app/
    main.py
    database.py
    models.py
    routers/
render.yaml
```

## Future Improvements

Authentication, personalized recommendations, advanced filtering, reading lists, reviews, and automated tests can be added as the product grows.
