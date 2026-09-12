from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routers import rutas, servicios, paraderos
from app.core.exceptions import NotFoundException, ValidationException, ConflictException

app = FastAPI(title="MS2 - Servicios", version="1.0.0")


@app.exception_handler(NotFoundException)
async def not_found_handler(request: Request, exc: NotFoundException):
    return JSONResponse(status_code=404, content={"detail": exc.detail})


@app.exception_handler(ValidationException)
async def validation_handler(request: Request, exc: ValidationException):
    return JSONResponse(status_code=400, content={"detail": exc.detail})


@app.exception_handler(ConflictException)
async def conflict_handler(request: Request, exc: ConflictException):
    return JSONResponse(status_code=409, content={"detail": exc.detail})


@app.get("/health")
async def health():
    return {"status": "ok"}


app.include_router(rutas.router)
app.include_router(servicios.router)
app.include_router(paraderos.router)