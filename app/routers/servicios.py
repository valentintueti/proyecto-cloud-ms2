from typing import Optional, List
from fastapi import APIRouter, Query
from app.schemas.servicio_schema import ServicioCreate, ServicioResponse
from app.services.servicio_service import servicio_service

router = APIRouter(prefix="/servicios", tags=["Servicios"])


@router.post("/", response_model=ServicioResponse, status_code=201)
async def crear_servicio(servicio: ServicioCreate):
    data = servicio.model_dump(mode="json")  # mode="json" serializa date/time a str
    return await servicio_service.crear_servicio(data)


@router.get("/", response_model=List[ServicioResponse])
async def listar_servicios(ruta_id: Optional[str] = None, fecha: Optional[str] = None):
    return await servicio_service.listar_servicios(ruta_id, fecha)


@router.get("/batch", response_model=List[ServicioResponse])
async def obtener_servicios_batch(ids: str = Query(..., description="ids separados por coma")):
    lista_ids = ids.split(",")
    return await servicio_service.obtener_servicios_batch(lista_ids)


@router.get("/{servicio_id}", response_model=ServicioResponse)
async def obtener_servicio(servicio_id: str):
    return await servicio_service.obtener_servicio(servicio_id)


@router.put("/{servicio_id}", response_model=ServicioResponse)
async def actualizar_servicio(servicio_id: str, cambios: ServicioCreate):
    data = cambios.model_dump(mode="json")
    return await servicio_service.actualizar_servicio(servicio_id, data)


@router.delete("/{servicio_id}", status_code=204)
async def eliminar_servicio(servicio_id: str):
    await servicio_service.eliminar_servicio(servicio_id)