from sqlalchemy import (Column, Float, ForeignKey, Integer, String, Table)
from sqlalchemy.orm import relationship, backref
from base import Base

biosample_2_treatment = Table('biosample_2_treatment',Base.metadata,
                      Column('treatment_accession',String(15),ForeignKey('treatment.treatment_accession')),
                      Column('biosample_accession',String(15),ForeignKey('biosample.biosample_accession'))
                      )


class Biosample(Base):
    __tablename__ = "biosample"

    biosample_accession = Column(String(15),primary_key=True,nullable=False)
    description = Column(String(4000))
    name = Column(String(200))
    planned_visit_accession = Column(String(15))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('biosamples'))
    study_time_collected = Column(Float(precision=12))
    study_time_collected_unit = Column(String(25))
    study_time_t0_event = Column(String(50))
    study_time_t0_event_specify = Column(String(50))
    subject_accession = Column(String(15),ForeignKey("subject.subject_accession"),nullable=False)
    subject = relationship("Subject",backref=backref('biosamples'))
    subtype = Column(String(50))
    type = Column(String(50))
    workspace_id = Column(Integer)

    treatments = relationship("Treatment",
                         secondary=biosample_2_treatment,
                         backref="biosamples")


    def __repr__(self):
        return "<Biosample(biosample_accession='%s', name='%s', type='%s'>" % (self.biosample_accession,self.name,self.type)
