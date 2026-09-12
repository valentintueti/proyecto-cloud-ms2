from typing import Optional, List
from app.models.enums import TipoServicio

class RutaResumen:
    def __init__(self, ruta_id: str, nombre: str, tipo_servicio: TipoServicio):
        self.ruta_id = ruta_id
        self.nombre = nombre
        self.tipo_servicio = tipo_servicio

    def to_dict(self) -> dict:
        return {
            "ruta_id": self.ruta_id,
            "nombre": self.nombre,
            "tipo_servicio": self.tipo_servicio.value
        }

class Paradero:
    def __init__(
        self,
        nombre: str,
        ubicacion: dict,
        rutas: List[RutaResumen],
        _id: Optional[str] = None
    ):
        self.id = _id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.rutas = rutas

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "rutas": [r.to_dict() for r in self.rutas]
        }