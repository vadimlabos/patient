from typing import Optional

from pydantic import BaseModel


class PatientIdSchema(BaseModel):
    iicode: Optional[int] = None
    iiid: Optional[str] = None
    iiidtype: Optional[int] = None
    iipid: Optional[str] = None

    class Config:
        from_attributes = True
