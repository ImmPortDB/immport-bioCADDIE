from sqlalchemy import (Column,  ForeignKey, Integer,
                        String, PrimaryKeyConstraint)
from sqlalchemy.orm import relationship, backref
from base import Base

class StudyPubmed(Base):
    __tablename__ = "study_pubmed"

    authors = Column(String(4000))
    doi = Column(String(100))
    issue = Column(String(20))
    journal = Column(String(250))
    month = Column(String(12))
    pages = Column(String(20))
    pubmed_id = Column(String(16))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('publications'))
    title = Column(String(4000))
    workspace_id = Column(Integer,nullable=False)
    year = Column(String(4))
    __table_args__ = (
        PrimaryKeyConstraint("study_accession","pubmed_id"),
    )

    def __repr__(self):
        return "<StudyPubMed(study_accession='%s', pubmed_id='%s',brief_title='%s'>" % (self.study_accession,self.pubmed_id,self.title)
