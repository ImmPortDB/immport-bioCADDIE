from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class LabTest(Base):
    __tablename__ = "lab_test"

    lab_test_accession = Column(String(15),primary_key=True,nullable=False)
    biosample_accession = Column(String(15),ForeignKey("biosample.biosample_accession"),nullable=False)
    biosample = relationship("Biosample",backref=backref('lab_tests'))
    lab_test_panel_accession = Column(String(15),ForeignKey("lab_test_panel.lab_test_panel_accession"),nullable=False)
    lab_test_panel = relationship("LabTestPanel",backref=backref('lab_tests'))
    name_preferred = Column(String(40))
    name_reported = Column(String(125))
    result_unit_preferred = Column(String(40))
    result_unit_reported = Column(String(40))
    result_value_preferred = Column(Float(precision=12))
    result_value_reported = Column(String(40))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<LabTest(lab_test_accession='%s', name_reported='%s'>" % (self.lab_test_accession,self.name_reported)
