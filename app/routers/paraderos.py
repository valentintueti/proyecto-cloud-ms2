from typing import List
from fastapi import APIRouter, Query
from app.schemas.paradero_schemas import (
    ParaderoCreate, ParaderoResponse, ValidaConexionResponse
)
from app.services.paradero_service import paradero_service

router = APIRouter(prefix="/paraderos", tags=["Paraderos"])


@router.post("/", response_model=ParaderoResponse, status_code=201)
async def crear_paradero(paradero: ParaderoCreate):
    data = paradero.model_dump()
    return await paradero_service.crear_paradero(data)


@router.get("/", response_model=List[ParaderoResponse])
async def listar_paraderos():
    return await paradero_service.listar_paraderos()


@router.get("/batch", response_model=List[ParaderoResponse])
async def obtener_paraderos_batch(ids: str = Query(..., description="ids separados por coma")):
    lista_ids = ids.split(",")
    return await paradero_service.obtener_paraderos_batch(lista_ids)


@router.get("/{paradero_id}", response_model=ParaderoResponse)
async def obtener_paradero(paradero_id: str):
    return await paradero_service.obtener_paradero(paradero_id)


@router.get("/{paradero_id}/valida-conexion", response_model=ValidaConexionResponse)
async def valida_conexion(paradero_id: str, ruta_id: str):
    es_valida = await paradero_service.valida_conexion(paradero_id, ruta_id)
    return {"paradero_id": paradero_id, "ruta_id": ruta_id, "es_valida": es_valida}