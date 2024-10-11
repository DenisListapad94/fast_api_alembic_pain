from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Integer, String, Table
from sqlalchemy.orm import Mapped,mapped_column

from src.database import Base

# note = Table(
#     "note",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("content", String),
#     Column("date", TIMESTAMP),
#     Column("type", String)
# )


class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    date: Mapped[datetime]
    type: Mapped[str]
