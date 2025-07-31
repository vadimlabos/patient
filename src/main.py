from fastapi import FastAPI
from src.routers import status, patient

app = FastAPI()
app.include_router(status.router)
app.include_router(patient.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8081)
