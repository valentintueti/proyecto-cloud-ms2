from typing import Optional, List
from app.database import paraderos_collection
from app.core.utils import generar_id, documento_a_dict


class ParaderoRepository:
    async def crear(self, data: dict) -> dict:
        paradero_id = generar_id("par")
        doc = {"_id": paradero_id, **data, "rutas": []}
        await paraderos_collection.insert_one(doc)
        return documento_a_dict(doc)

    async def obtener_por_id(self, paradero_id: str) -> Optional[dict]:
        doc = await paraderos_collection.find_one({"_id": paradero_id})
        return documento_a_dict(doc)

    async def listar(self) -> List[dict]:
        cursor = paraderos_collection.find({})
        return [documento_a_dict(doc) async for doc in cursor]

    async def find_by_ids(self, ids: List[str]) -> List[dict]:
        cursor = paraderos_collection.find({"_id": {"$in": ids}})
        return [documento_a_dict(doc) async for doc in cursor]

    async def agregar_ruta(self, paradero_id: str, ruta_resumen: dict) -> None:
        await paraderos_collection.update_one(
            {"_id": paradero_id},
            {"$addToSet": {"rutas": ruta_resumen}}
        )

    async def quitar_ruta(self, paradero_id: str, ruta_id: str) -> None:
        await paraderos_collection.update_one(
            {"_id": paradero_id},
            {"$pull": {"rutas": {"ruta_id": ruta_id}}}
        )

    async def existe_ruta_en_paradero(self, paradero_id: str, ruta_id: str) -> bool:
        doc = await paraderos_collection.find_one({
            "_id": paradero_id,
            "rutas.ruta_id": ruta_id
        })
        return doc is not None


paradero_repository = ParaderoRepository()