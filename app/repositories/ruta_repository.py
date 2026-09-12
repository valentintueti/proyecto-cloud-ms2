from typing import Optional, List
from app.database import rutas_collection
from app.core.utils import generar_id, documento_a_dict


class RutaRepository:
    async def crear(self, data: dict) -> dict:
        ruta_id = generar_id("R")
        doc = {"_id": ruta_id, **data}
        await rutas_collection.insert_one(doc)
        return documento_a_dict(doc)

    async def obtener_por_id(self, ruta_id: str) -> Optional[dict]:
        doc = await rutas_collection.find_one({"_id": ruta_id})
        return documento_a_dict(doc)

    async def listar(self, tipo_servicio: Optional[str] = None) -> List[dict]:
        filtro = {"tipo_servicio": tipo_servicio} if tipo_servicio else {}
        cursor = rutas_collection.find(filtro)
        return [documento_a_dict(doc) async for doc in cursor]

    async def find_by_ids(self, ids: List[str]) -> List[dict]:
        cursor = rutas_collection.find({"_id": {"$in": ids}})
        return [documento_a_dict(doc) async for doc in cursor]

    async def actualizar(self, ruta_id: str, cambios: dict) -> Optional[dict]:
        await rutas_collection.update_one({"_id": ruta_id}, {"$set": cambios})
        return await self.obtener_por_id(ruta_id)

    async def eliminar(self, ruta_id: str) -> bool:
        resultado = await rutas_collection.delete_one({"_id": ruta_id})
        return resultado.deleted_count > 0


ruta_repository = RutaRepository()