from typing import Annotated

from fastapi import APIRouter, Query, HTTPException

from src.controllers.patient import Controller
from src.models.patient import Patient
from src.schemas.patient import PatientSchema

router: APIRouter = APIRouter()
controller: Controller = Controller()


@router.get("/patient", response_model= PatientSchema | list[PatientSchema] | None)
async def get_patient(
        code: Annotated[int | None, Query()] = None,
        string: Annotated[str | None, Query(min_length=1, max_length=20)] = None):

    patient: list[Patient] | None = None
    if code is not None and code > 0:
        patient = await controller.get_patient_by_code(code)

    if string is not None:
        patient = await controller.get_patient_by_string(string)

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient
