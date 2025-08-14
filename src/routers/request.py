from fastapi import APIRouter, Depends
from src.controllers.request import RequestController
from src.dependences.dependences import get_request_controller
from src.models.request import Request
from src.schemas.request import RequestSchema

router: APIRouter = APIRouter()


@router.get("/request-async", response_model=RequestSchema | list[RequestSchema] | None)
async def get_results(
        controller: RequestController = Depends(get_request_controller)):
    return await controller.get_requests_async()
