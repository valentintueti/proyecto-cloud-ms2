from typing import List
from app.repositories.paradero_repository import paradero_repository
from app.core.exceptions import NotFoundException


class ParaderoService:
    async def crear_paradero(self, data: dict) -> dict:
        return await paradero_repository.crear(data)

    async def obtener_paradero(self, paradero_id: str) -> dict:
        paradero = await paradero_repository.obtener_por_id(paradero_id)
        if not paradero:
            raise NotFoundException(f"Paradero {paradero_id} no encontrado")
        return paradero

    async def listar_paraderos(self) -> List[dict]:
        return await paradero_repository.listar()

    async def obtener_paraderos_batch(self, ids: List[str]) -> List[dict]:
        return await paradero_repository.find_by_ids(ids)

    async def agregar_ruta_a_paradero(self, paradero_id: str, ruta_resumen: dict) -> None:
        await self.obtener_paradero(paradero_id)
        await paradero_repository.agregar_ruta(paradero_id, ruta_resumen)

    async def quitar_ruta_de_paradero(self, paradero_id: str, ruta_id: str) -> None:
        await self.obtener_paradero(paradero_id)
        await paradero_repository.quitar_ruta(paradero_id, ruta_id)

    async def valida_conexion(self, paradero_id: str, ruta_id: str) -> bool:
        await self.obtener_paradero(paradero_id)
        return await paradero_repository.existe_ruta_en_paradero(paradero_id, ruta_id)


paradero_service = ParaderoService()