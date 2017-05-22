from sqlalchemy import (Column,  ForeignKey, Integer, String)
from sqlalchemy.orm import relationship, backref
from base import Base

class Experiment(Base):
    __tablename__ = "experiment"

    experiment_accession = Column(String(15),primary_key=True,nullable=False)
    description = Column(String(4000))
    measurement_technique = Column(String(50))
    name = Column(String(500))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('experiments'))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<Experiment(experiment_accession='%s', name='%s'>" % (self.experiment_accession,self.name)
