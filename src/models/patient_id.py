from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mssql import TINYINT
from src.db.database import Base
from sqlalchemy.sql import quoted_name
from src.config.settings import get_general_settings


class Identifier(Base):
    __tablename__ = quoted_name(get_general_settings().patient_id_table, quote=True)  # replace with actual name

    iicode = Column(Integer, primary_key=True)
    iiid = Column(String(22), nullable=False)
    iiidtype = Column(TINYINT, nullable=False)
    iipid = Column(String(100), nullable=False)