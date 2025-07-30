from sqlalchemy import Column, Integer, String, SmallInteger
from sqlalchemy.sql import quoted_name

from src.config.settings import get_general_settings
from src.db.database import Base


class Episode(Base):
    __tablename__ = quoted_name(get_general_settings().episode_table, quote=True)

    eptype = Column(SmallInteger,primary_key=True, nullable=False)
    epcode = Column(String(100),primary_key=True, nullable=False)
    epdate = Column(Integer, nullable=False)
    eptime = Column(SmallInteger, nullable=True)
    epid = Column(String(40), nullable=False)
    epclosedate = Column(Integer, nullable=True)
    epclosetime = Column(SmallInteger, nullable=True)
    epcommconst = Column(SmallInteger, nullable=True)
    epcommfree = Column(SmallInteger, nullable=True)
    epnumber = Column(Integer, nullable=True)
    eppatcode = Column(Integer, nullable=True)
    epextfield1 = Column(Integer, nullable=True)
    epextfield2 = Column(Integer, nullable=True)
    epextfield3 = Column(Integer, nullable=True)
    epsite = Column(Integer, nullable=True)
