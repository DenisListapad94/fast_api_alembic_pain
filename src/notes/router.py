from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.notes.models import Note
from src.notes.schemas import NoteCreate

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.get("/")
async def get_specific_notes(note_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Note).where(Note.c.type == note_type)
    result = await session.execute(query)

    # Преобразование результатов в список словарей
    notes_dicts = [row._asdict() for row in result.all()]
    return {"result": notes_dicts}


@router.post("/")
async def add_note(new_note: NoteCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Note).values(new_note.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"result": "success"}
