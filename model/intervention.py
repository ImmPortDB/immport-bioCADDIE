from sqlalchemy import (Column, DateTime, ForeignKey, Integer,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class Intervention(Base):
    __tablename__ = "intervention"

    intervention_accession = Column(String(15),primary_key=True,nullable=False)
    compound_name_reported = Column(String(250))
    compound_role = Column(String(40))
    dose = Column(Float(precision=12))
    dose_freq_per_interval = Column(String(40))
    dose_reported = Column(String(150))
    dose_units = Column(String(40))
    duration = Column(Float(precision=12))
    duration_unit = Column(String(10))
    end_day = Column(Float(precision=12))
    end_time = Column(String(40))
    formulation = Column(String(125))
    is_ongoing = Column(String(40))
    name_preferred = Column(String(40))
    name_reported = Column(String(125))
    reported_indication = Column(String(255))
    route_of_admin_preferred = Column(String(40))
    route_of_admin_reported = Column(String(40))
    start_day = Column(Float(precision=12))
    start_time = Column(String(40))
    status = Column(String(40))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('interventions'))
    subject_accession = Column(String(15),ForeignKey("subject.subject_accession"),nullable=False)
    subject = relationship("Subject",backref=backref('interventions'))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<Intervention(intervention_accession='%s', name_reported='%s'>" % (self.intervention_accession,self.name_reported)
