from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship, backref
from base import Base

class Program(Base):
    __tablename__ = "program"

    program_id = Column(Integer,primary_key=True,nullable=False)
    category = Column(String(50))
    description = Column(String(4000))
    end_date = Column(DateTime)
    link = Column(String(2000))
    name = Column(String(200))
    start_date = Column(DateTime)

    def __repr__(self):
        return "<Program(program_id='%s', name='%s')>" % (self.program_id,self.name)
