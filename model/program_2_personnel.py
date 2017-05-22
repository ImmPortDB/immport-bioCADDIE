from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class Program2Personnel(Base):
    __tablename__ = "program_2_personnel"
  
    personnel_id = Column(Integer))
    program_id = Column(Integer))
    role_type = Column(String(12))
