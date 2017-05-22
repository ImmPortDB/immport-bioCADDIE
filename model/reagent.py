from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship, backref
from base import Base

class Reagent(Base):
    __tablename__ = "reagent"

    reagent_accession = Column(String(15),primary_key=True,nullable=False)
    analyte_preferred = Column(String(200))
    analyte_reported = Column(String(200))
    antibody_registry_id = Column(String(250))
    catalog_number = Column(String(250))
    clone_name = Column(String(200))
    contact = Column(String(1000))
    description = Column(String(4000))
    is_set = Column(String(1))
    lot_number = Column(String(250))
    manufacturer = Column(String(100))
    name = Column(String(200))
    reporter_name = Column(String(200))
    type = Column(String(50))
    weblink = Column(String(250))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<Reagent(reagent_accession='%s')>" % (self.reagent_accession)
