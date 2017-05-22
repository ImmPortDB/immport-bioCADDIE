from sqlalchemy import (Column, ForeignKey, Integer, String)
from sqlalchemy.orm import relationship, backref
from base import Base

class InclusionExclusion(Base):
    __tablename__ = "inclusion_exclusion"

    criterion_accession = Column(String(15),primary_key=True,nullable=False)
    criterion = Column(String(750))
    criterion_category = Column(String(40))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('inclusion_exclusions'))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<InclusionExclusion(criterion_accession='%s', criterion='%s'>" % (self.criterion_accession,self.criterion)
