from sqlalchemy import (Column, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship, backref
from base import Base


class StudyCategorization(Base):
    __tablename__ = "study_categorization"

    study_categorization_id = Column(Integer, primary_key=True, nullable=False)
    research_focus = Column(String(50))
    study_accession = Column(String(15), ForeignKey(
        "study.study_accession"), nullable=False)
    study = relationship("Study", backref=backref('categorizations'))

    def __repr__(self):
        return "<StudyCategorization(study_accession='%s', research_focus='%s'>" % (self.study_accession, self.research_focus)
