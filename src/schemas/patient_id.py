from typing import Optional

from pydantic import BaseModel, ConfigDict


class PatientIdSchema(BaseModel):
    iicode: Optional[int] = None
    iiid: Optional[str] = None
    iiidtype: Optional[int] = None
    iipid: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
