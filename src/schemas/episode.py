from pydantic import BaseModel, ConfigDict
from typing import Optional


class EpisodeSchema(BaseModel):
    eptype: Optional[int] = None
    epcode: Optional[str] = None
    epdate: Optional[int] = None
    eptime: Optional[int] = None
    epid: Optional[str] = None
    epclosedate: Optional[int] = None
    epclosetime: Optional[int] = None
    epcommconst: Optional[int] = None
    epcommfree: Optional[int] = None
    epnumber: Optional[int] = None
    eppatcode: Optional[int] = None
    epextfield1: Optional[int] = None
    epextfield2: Optional[int] = None
    epextfield3: Optional[int] = None
    epsite: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)
