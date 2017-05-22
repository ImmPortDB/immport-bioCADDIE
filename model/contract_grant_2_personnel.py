from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class ContractGrant2Personnel(Base):
    __tablename__ = "contract_grant_2_personnel"

    contract_grant_id = Column(Integer,ForeignKey('contract_grant.contract_grant_id'),primary_key=True)
    personnel_id = Column(Integer,ForeignKey('personnel.personnel_id'),primary_key=True)
    role_type = Column(String(12))

    contract = relationship("ContractGrant",backref="personnel")
    personnel = relationship("Personnel",backref="contract_grants")

    def __repr__(self):
        return "<ContractGrant2Personnel(contract_grant_id)='%s', personnel_id='%s'>" % (self.contract_grant_id,self.personnel_id)
