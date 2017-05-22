from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class ElispotResult(Base):
    __tablename__ = "elispot_result"

    result_id = Column(Integer,primary_key=True,nullable=False)
    analyte_preferred = Column(String(100))
    analyte_reported = Column(String(100))
    arm_accession = Column(String(15),ForeignKey("arm_or_cohort.arm_accession"),nullable=False)
    arm = relationship("ArmOrCohort",backref=backref('elispot_results'))
    biosample_accession = Column(String(15),ForeignKey("biosample.biosample_accession"),nullable=False)
    biosample = relationship("Biosample",backref=backref('elispot_results'))
    cell_number_preferred = Column(Float(precision=12))
    cell_number_reported = Column(String(50))
    comments = Column(String(500))
    experiment_accession = Column(String(15),ForeignKey("experiment.experiment_accession"),nullable=False)
    experiment = relationship("Experiment",backref=backref('elispot_results'))
    expsample_accession = Column(String(15),ForeignKey("expsample.expsample_accession"),nullable=False)
    expsample = relationship("Expsample",backref=backref('elispot_results'))
    spot_number_preferred = Column(Float(precision=12))
    spot_number_reported = Column(String(50))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('elispot_results'))
    study_time_collected = Column(Float(precision=12))
    study_time_collected_unit = Column(String(25))
    subject_accession = Column(String(15),ForeignKey("subject.subject_accession"),nullable=False)
    subject = relationship("Subject",backref=backref('elispot_results'))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<ElispotResult(result_id='%s', analyte_reported='%s'>" % (self.result_id,self.analyte_reported)
