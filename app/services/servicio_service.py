from typing import Optional, List
from app.repositories.servicio_repository import servicio_repository
from app.repositories.ruta_repository import ruta_repository
from app.services.paradero_service import paradero_service
from app.core.exceptions import NotFoundException, ValidationException


class ServicioService:
    async def crear_servicio(self, data: dict) -> dict:
        # 1. Validar que la ruta exista antes de crear el servicio
        ruta = await ruta_repository.obtener_por_id(data["ruta_id"])
        if not ruta:
            raise ValidationException(f"La ruta {data['ruta_id']} no existe")

        # 2. Crear el servicio
        servicio = await servicio_repository.crear(data)

        # 3. Propagar la ruta a cada paradero involucrado
        ruta_resumen = {
            "ruta_id": ruta["id"],
            "nombre": ruta["nombre"],
            "tipo_servicio": ruta["tipo_servicio"]
        }
        for p in data["paraderos"]:
            await paradero_service.agregar_ruta_a_paradero(p["paradero_id"], ruta_resumen)

        return servicio

    async def obtener_servicio(self, servicio_id: str) -> dict:
        servicio = await servicio_repository.obtener_por_id(servicio_id)
        if not servicio:
            raise NotFoundException(f"Servicio {servicio_id} no encontrado")
        return servicio

    async def listar_servicios(self, ruta_id: Optional[str] = None, fecha: Optional[str] = None) -> List[dict]:
        return await servicio_repository.listar(ruta_id, fecha)

    async def obtener_servicios_batch(self, ids: List[str]) -> List[dict]:
        return await servicio_repository.find_by_ids(ids)

    async def actualizar_servicio(self, servicio_id: str, cambios: dict) -> dict:
        await self.obtener_servicio(servicio_id)
        return await servicio_repository.actualizar(servicio_id, cambios)

    async def eliminar_servicio(self, servicio_id: str) -> None:
        eliminado = await servicio_repository.eliminar(servicio_id)
        if not eliminado:
            raise NotFoundException(f"Servicio {servicio_id} no encontrado")


servicio_service = ServicioService()