from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class Arm2Subject(Base):
    __tablename__ = "arm_2_subject"

    arm_accession = Column(String(15),ForeignKey('arm_or_cohort.arm_accession'),primary_key=True)
    subject_accession = Column(String(15),ForeignKey('subject.subject_accession'),primary_key=True)

    age_event = Column(String(50))
    age_event_specify = Column(String(50))
    age_unit = Column(String(50))
    max_subject_age = Column(Float(precision=12))
    min_subject_age = Column(Float(precision=12))
    subject_phenotype = Column(String(200))

    arm = relationship("ArmOrCohort",backref='subjects')
    subject = relationship("Subject",backref="arms")
