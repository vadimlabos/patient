from typing import Annotated

from fastapi import APIRouter, Query, HTTPException
from src.schemas.patient import PatientSchema
from src.controllers.patient import Controller

router: APIRouter = APIRouter()


@router.get("/patient", response_model=PatientSchema | None)
def get_patient(code: Annotated[int | None, Query()] = None):
    patient = Controller.get_patient_by_code(code)

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient
