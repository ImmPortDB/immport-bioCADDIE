from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base
from marshmallow import Schema

class StudyPersonnel(Base):
    __tablename__ = "study_personnel"

    person_accession = Column(String(15),primary_key=True,nullable=False)
    email = Column(String(40))
    first_name = Column(String(40))
    honorific = Column(String(20))
    last_name = Column(String(40))
    organization = Column(String(125))
    role_in_study = Column(String(40))
    site_name = Column(String(100))
    study_accession = Column(String(15),ForeignKey("study.study_accession"),nullable=False)
    study = relationship("Study",backref=backref('personnel'))
    suffixes = Column(String(40))
    title_in_study = Column(String(100))
    workspace_id = Column(Integer)

    def __repr__(self):
        return "<StudyPersonnel(person_accession='%s', first_name='%s', last_name='%s'>" % (self.person_accession, self.first_name,self.last_name)

class StudyPersonnelSchema(Schema):
    class Meta:
        fields = ['person_accession','email','first_name','honorific',
                  'last_name','organization','role_in_study','site_name',
                  'study_accession','suffixes','title_in_study']
