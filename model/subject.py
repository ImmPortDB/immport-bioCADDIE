from sqlalchemy import (Column, ForeignKey, Integer,
                        String, Table)
from sqlalchemy.orm import relationship, backref
from base import Base

#arm_2_subject = Table('arm_2_subject',Base.metadata,
#                      Column('arm_accession',String(15),ForeignKey('arm_or_cohort.arm_accession')),
#                      Column('subject_accession',String(15),ForeignKey('subject.subject_accession'))
#                     )

class Subject(Base):
    __tablename__ = "subject"

    subject_accession = Column(String(15),primary_key=True,nullable=False)
    ancestral_population = Column(String(100))
    description = Column(String(4000))
    ethnicity = Column(String(50))
    gender = Column(String(20))
    race = Column(String(50))
    race_specify = Column(String(1000))
    species = Column(String(50))
    strain = Column(String(50))
    strain_characteristics = Column(String(500))
    workspace_id = Column(Integer)

#    arm = relationship("ArmOrCohort",
#                         secondary=arm_2_subject,
#                         backref="subjects")

    def __repr__(self):
        return "<Subject(subject_accession='%s'>" % (self.subject_accession)
