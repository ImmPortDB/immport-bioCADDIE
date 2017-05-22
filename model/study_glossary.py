from sqlalchemy import (Column, ForeignKey, Integer, PrimaryKeyConstraint, String)
from sqlalchemy.orm import relationship, backref
from base import Base

class StudyGlossary(Base):
    __tablename__ = "study_glossary"

    definition = Column(String(500))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('glossaries'))
    term = Column(String(125))
    workspace_id = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("study_accession","term"),
    )

    def __repr__(self):
        return "<StudyGlossary(study_accession='%s', term='%s'>" % (self.study_accession,self.term)
