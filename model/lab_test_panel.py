from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class LabTestPanel(Base):
    __tablename__ = "lab_test_panel"

    lab_test_panel_accession = Column(String(15),primary_key=True,nullable=False)
    name_preferred = Column(String(40))
    name_reported = Column(String(40))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('lab_test_panels'))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<LabTestPanel(lab_test_panel_accession='%s', name_reported='%s'>" % (self.lab_test_panel_accession,self.name_reported)
