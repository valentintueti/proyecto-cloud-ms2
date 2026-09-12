from typing import Optional
from app.models.enums import TipoServicio, Sentido

class Ruta:
    def __init__(
        self,
        nombre: str,
        tipo_servicio: TipoServicio,
        sentido: Sentido,
        _id: Optional[str] = None
    ):
        self.id = _id
        self.nombre = nombre
        self.tipo_servicio = tipo_servicio
        self.sentido = sentido

    def to_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "tipo_servicio": self.tipo_servicio.value,
            "sentido": self.sentido.value
        }