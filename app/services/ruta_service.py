from typing import Optional, List
from app.repositories.ruta_repository import ruta_repository
from app.core.exceptions import NotFoundException


class RutaService:
    async def crear_ruta(self, data: dict) -> dict:
        return await ruta_repository.crear(data)

    async def obtener_ruta(self, ruta_id: str) -> dict:
        ruta = await ruta_repository.obtener_por_id(ruta_id)
        if not ruta:
            raise NotFoundException(f"Ruta {ruta_id} no encontrada")
        return ruta

    async def listar_rutas(self, tipo_servicio: Optional[str] = None) -> List[dict]:
        return await ruta_repository.listar(tipo_servicio)

    async def obtener_rutas_batch(self, ids: List[str]) -> List[dict]:
        return await ruta_repository.find_by_ids(ids)

    async def actualizar_ruta(self, ruta_id: str, cambios: dict) -> dict:
        await self.obtener_ruta(ruta_id)
        return await ruta_repository.actualizar(ruta_id, cambios)

    async def eliminar_ruta(self, ruta_id: str) -> None:
        eliminado = await ruta_repository.eliminar(ruta_id)
        if not eliminado:
            raise NotFoundException(f"Ruta {ruta_id} no encontrada")


ruta_service = RutaService()