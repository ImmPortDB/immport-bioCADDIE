from sqlalchemy import (Column, DateTime, ForeignKey, Integer,  String)
from sqlalchemy.orm import relationship, backref
from base import Base

class Treatment(Base):
    __tablename__ = "treatment"

    treatment_accession = Column(String(15),primary_key=True,nullable=False)
    amount_unit = Column(String(50))
    amount_value = Column(String(50))
    comments = Column(String(500))
    duration_unit = Column(String(50))
    duration_value = Column(String(200))
    name = Column(String(100))
    temperature_unit = Column(String(50))
    temperature_value = Column(String(50))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<Treatement(treatment_accession='%s', name='%s'>" % (self.treatment_accession,self.name)
