from sqlalchemy import Column, DateTime, String, Text
from database import Base

class Notebooks(Base):
    ts = Column(String(13), primary_key=True)
    bookname = Column(String(20))

    def __init__(self, ts=None, bookname=None):
        self.ts = ts
        self.bookname = bookname

    def __repr__(self):
        return f'<{self.bookname} %r>'


class NoteInfo(Base):
    ts = Column(DateTime, primary_key=True)
    bookid = Column(String(13))
    note = Column(Text)

    def __init__(self, ts=None, bookid=None, note=None):
        self.ts = ts
        self.bookid = bookid
        self.note = note

    def __repr__(self):
        return f'<{self.note} %r>'
