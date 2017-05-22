from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship, backref
from base import Base

class AssessmentPanel(Base):
    __tablename__ = "assessment_panel"

    assessment_panel_accession = Column(String(15),primary_key=True,nullable=False)
    assessment_type = Column(String(125))
    name_preferred = Column(String(40))
    name_reported = Column(String(125))
    status = Column(String(40))
    study_accession = Column(String(15))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('assessment_panels'))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<AssessmentPanel(assessment_panel_accession='%s', name_reported='%s'>" % (self.assessment_panel_accession,self.name_reported)
