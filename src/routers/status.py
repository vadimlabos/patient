from fastapi import APIRouter

router = APIRouter()


@router.get("/status", status_code=200)
def status() -> dict[str, str]:
    return {"status": "running"}