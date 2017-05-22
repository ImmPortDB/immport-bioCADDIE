from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base

class ContractGrant2Study(Base):
    __tablename__ = "contract_grant_2_study"
  
    contract_grant_id = Column(Integer))
    study_accession = Column(String(15))
