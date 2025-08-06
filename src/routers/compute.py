from fastapi import APIRouter, Depends

from src.controllers.compute import ComputeController
from src.dependences.dependences import get_compute_controller

router: APIRouter = APIRouter()


@router.get("/compute", status_code=200)
async def compute(
        controller: ComputeController = Depends(get_compute_controller)
):
    await controller.compute()
    return {"Compute finished"}
