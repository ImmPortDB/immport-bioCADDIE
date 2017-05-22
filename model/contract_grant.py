from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text, Table)
from sqlalchemy.orm import relationship, backref
from base import Base

contract_grant_2_study = Table('contract_grant_2_study',Base.metadata,
                               Column('contract_grant_id',Integer,
                                      ForeignKey('contract_grant.contract_grant_id')),
                               Column('study_accession',String(15),
                                      ForeignKey('study.study_accession'))
                            )
#contract_grant_2_personnel = Table('contract_grant_2_personnel',Base.metadata,
#                                   Column('contract_grant_id',Integer,
#                                          ForeignKey('contract_grant.contract_grant_id')),
#                                   Column('personnel_id',Integer,
#                                          ForeignKey('personnel.personnel_id'))
#                                  )

class ContractGrant(Base):
    __tablename__ = "contract_grant"

    contract_grant_id = Column(Integer,primary_key=True,nullable=False)
    category = Column(String(50))
    description = Column(String(4000))
    end_date = Column(DateTime)
    external_id = Column(String(50))
    link = Column(String(2000))
    name = Column(String(1000))
    program_id = Column(Integer,ForeignKey("program.program_id"))
    program = relationship("Program",backref=backref('contract'))

    start_date = Column(DateTime)

    studies = relationship('Study',
            secondary=contract_grant_2_study,
            backref='contracts')

#    personnel = relationship('Personnel',
#                secondary=contract_grant_2_personnel,
#                backref='contracts')

    def __repr__(self):
        return "<ContratGrant(contract_grant_id='%s',name='%s'>" % (self.contract_grant_id, self.name)
