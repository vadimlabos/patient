from fastapi import FastAPI
from src.routers import status, patient, compute, request

app = FastAPI()
app.include_router(status.router)
app.include_router(patient.router)
app.include_router(compute.router)
app.include_router(request.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8081, log_level="error", access_log=False, workers=25)
