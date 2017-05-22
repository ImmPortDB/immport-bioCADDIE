from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class ArmOrCohort(Base):
    __tablename__ = "arm_or_cohort"

    arm_accession = Column(String(15),primary_key=True,nullable=False)
    description = Column(String(4000))
    name = Column(String(126))
    study_accession = Column(String(15),ForeignKey('study.study_accession'),nullable=False)
    study = relationship("Study",backref=backref('arms'))
    type = Column(String(20))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<ArmOrCohort(arm_accession='%s'>)" % (self.arm_accession)
