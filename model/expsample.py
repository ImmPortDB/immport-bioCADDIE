from sqlalchemy import (Column,  ForeignKey, Integer, String)
from sqlalchemy.orm import relationship, backref
from base import Base

class Expsample(Base):
    __tablename__ = "expsample"

    expsample_accession = Column(String(15),primary_key=True,nullable=False)
    description = Column(String(4000))
    experiment_accession = Column(String(15),ForeignKey("experiment.experiment_accession"),nullable=False)
    experiment = relationship("Experiment",backref=backref('expsamples'))
    name = Column(String(200))
    result_schema = Column(String(50))
    upload_result_status = Column(String(20))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<Expsample(expsample_accession='%s', name='%s'>" % (self.expsample_accession,self.name)
