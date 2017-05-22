from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base
from marshmallow import Schema


class Study(Base):
    __tablename__ = "study"

    study_accession = Column(String(15), primary_key=True, nullable=False)
    actual_completion_date = Column(DateTime)
    actual_enrollment = Column(Integer)
    actual_start_date = Column(DateTime)
    age_unit = Column(String(40))
    brief_description = Column(String(4000))
    brief_title = Column(String(250))
    clinical_trial = Column(String(1), nullable=False, default="N")
    condition_studied = Column(String(1000))
    dcl_id = Column(Integer, nullable=False, default=0)
    description = Column(Text)
    doi = Column(String(100))
    endpoints = Column(Text)
    gender_included = Column(String(50))
    hypothesis = Column(String(4000))
    initial_data_release_date = Column(DateTime)
    initial_data_release_version = Column(String(10))
    intervention_agent = Column(String(1000))
    latest_data_release_date = Column(DateTime)
    latest_data_release_version = Column(String(10))
    maximum_age = Column(String(40))
    minimum_age = Column(String(40))
    objectives = Column(Text)
    official_title = Column(String(500))
    sponsoring_organization = Column(String(250))
    target_enrollment = Column(Integer)
    type = Column(String(50), nullable=False)
    workspace_id = Column(Integer, ForeignKey(
        "workspace.workspace_id"), nullable=False)
    workspace = relationship("Workspace", backref=backref('studies'))

    def __repr__(self):
        return "<Study(study_accession='%s',brief_title='%s'>" % (self.study_accession, self.brief_title)

class StudySchema(Schema):
    class Meta:
        fields = ['study_accession','brief_title','brief_description','doi']
