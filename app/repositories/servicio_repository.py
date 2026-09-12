from typing import Optional, List
from app.database import servicios_collection
from app.core.utils import generar_id, documento_a_dict


class ServicioRepository:
    async def crear(self, data: dict) -> dict:
        servicio_id = generar_id("srv")
        doc = {"_id": servicio_id, **data}
        await servicios_collection.insert_one(doc)
        return documento_a_dict(doc)

    async def obtener_por_id(self, servicio_id: str) -> Optional[dict]:
        doc = await servicios_collection.find_one({"_id": servicio_id})
        return documento_a_dict(doc)

    async def listar(self, ruta_id: Optional[str] = None, fecha: Optional[str] = None) -> List[dict]:
        filtro = {}
        if ruta_id:
            filtro["ruta_id"] = ruta_id
        if fecha:
            filtro["fecha"] = fecha
        cursor = servicios_collection.find(filtro)
        return [documento_a_dict(doc) async for doc in cursor]

    async def find_by_ids(self, ids: List[str]) -> List[dict]:
        cursor = servicios_collection.find({"_id": {"$in": ids}})
        return [documento_a_dict(doc) async for doc in cursor]

    async def actualizar(self, servicio_id: str, cambios: dict) -> Optional[dict]:
        await servicios_collection.update_one({"_id": servicio_id}, {"$set": cambios})
        return await self.obtener_por_id(servicio_id)

    async def eliminar(self, servicio_id: str) -> bool:
        resultado = await servicios_collection.delete_one({"_id": servicio_id})
        return resultado.deleted_count > 0


servicio_repository = ServicioRepository()