from sqlalchemy import (Column, Integer, String)
from base import Base

class Personnel(Base):
    __tablename__ = "personnel"

    email = Column(String(100))
    first_name = Column(String(50))
    last_name = Column(String(50))
    organization = Column(String(125))
    personnel_id = Column(Integer,primary_key=True,nullable=False)

    def __repr__(self):
        return "<Personnel(personnel_id='%s', first_name='%s', last_name='%s'>" % (self.personnel_id, self.first_name,self.last_name)
