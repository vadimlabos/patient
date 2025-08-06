from typing import Annotated

from fastapi import APIRouter, Query, HTTPException, Depends

from src.controllers.patient import PatientController
from src.dependences.dependences import get_patient_controller
from src.models.patient import Patient
from src.schemas.patient import PatientSchema

router: APIRouter = APIRouter()


@router.get("/patient-async", response_model=PatientSchema | list[PatientSchema] | None)
async def get_patient(
        controller: PatientController = Depends(get_patient_controller),
        code: Annotated[int | None, Query()] = None,
        searchString: Annotated[str | None, Query(min_length=1, max_length=20)] = None):

    patient: list[Patient] | None = None
    if code is not None and code > 0:
        patient = await controller.get_patient_by_code_async(code)

    if searchString is not None:
        patient = await controller.get_patient_by_string_async(searchString)

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


@router.get("/patient", response_model=PatientSchema | list[PatientSchema] | None)
def get_patient(
        controller: PatientController = Depends(get_patient_controller),
        code: Annotated[int | None, Query()] = None,
        searchString: Annotated[str | None, Query(min_length=1, max_length=20)] = None):

    patient: list[Patient] | None = None
    if code is not None and code > 0:
        patient = controller.get_patient_by_code(code)

    if searchString is not None:
        patient = controller.get_patient_by_string(searchString)

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient
