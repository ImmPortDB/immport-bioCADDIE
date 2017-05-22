from sqlalchemy import (Column, DateTime, ForeignKey, Integer, Numeric,
                        Float, String, Text)
from sqlalchemy.orm import relationship, backref
from base import Base


class Workspace(Base):
    __tablename__ = "workspace"

    workspace_id = Column(Integer, primary_key=True, nullable=False)
    category = Column(String(50))
    name = Column(String(125))
    type = Column(String(20))


    def __repr__(self):
        return "<Workspace(workspace_id='%d', name='%s'>" % (self.workspace_id, self.name)
