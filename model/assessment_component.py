from sqlalchemy import (Column, DateTime, ForeignKey, Integer,
                        Float, String)
from sqlalchemy.orm import relationship, backref
from base import Base

class AssessmentComponent(Base):
    __tablename__ = "assessment_component"

    assessment_component_accession = Column(String(15),primary_key=True,nullable=False)
    age_at_onset_preferred = Column(Float(precision=12))
    age_at_onset_reported = Column(String(100))
    age_at_onset_unit_preferred = Column(String(40))
    age_at_onset_unit_reported = Column(String(25))
    assessment_panel_accession = Column(String(15),ForeignKey("assessment_panel.assessment_panel_accession"),nullable=False)
    assessment_panel = relationship("AssessmentPanel",backref=backref('assessment_components'))
    is_clinically_significant = Column(String(1))
    location_of_finding_preferred = Column(String(256))
    location_of_finding_reported = Column(String(256))
    name_preferred = Column(String(150))
    name_reported = Column(String(150))
    organ_or_body_system_preferred = Column(String(100))
    organ_or_body_system_reported = Column(String(100))
    planned_visit_accession = Column(String(15))
    reference_range_accession = Column(String(15))
    result_unit_preferred = Column(String(40))
    result_unit_reported = Column(String(40))
    result_value_category = Column(String(40))
    result_value_preferred = Column(Float(precision=12))
    result_value_reported = Column(String(250))
    study_day = Column(Float(precision=12))
    subject_accession = Column(String(15),ForeignKey("subject.subject_accession"),nullable=False)
    subject = relationship("Subject",backref=backref('assessment_components'))
    subject_position_preferred = Column(String(40))
    subject_position_reported = Column(String(40))
    time_of_day = Column(String(40))
    verbatim_question = Column(String(250))
    who_is_assessed = Column(String(40))
    workspace_id = Column(Integer)

    def __repr__(self):
        return ("<AssessmentComponent(assessment_component_accession='%s', result_value_reported='%s', result_unit_reported='%s'>" %
                (self.assessment_component_accession,
                 self.result_value_reported,self.result_unit_reported))
