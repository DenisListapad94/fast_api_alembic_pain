from fastapi import FastAPI

from src.notes.router import router as notes_router

app = FastAPI(title="Demo Fast API")
app.include_router(notes_router)


@app.get('/')
def hello():
    return "Hello world!"
