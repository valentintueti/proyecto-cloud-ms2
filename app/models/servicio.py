from typing import Optional, List
from datetime import date, time

class ParaderoOrden:
    def __init__(self, paradero_id: str, orden: int):
        self.paradero_id = paradero_id
        self.orden = orden

    def to_dict(self) -> dict:
        return {"paradero_id": self.paradero_id, "orden": self.orden}

class Servicio:
    def __init__(
        self,
        ruta_id: str,
        fecha: date,
        hora_inicio: time,
        hora_fin: time,
        paraderos: List[ParaderoOrden],
        _id: Optional[str] = None
    ):
        self.id = _id
        self.ruta_id = ruta_id
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.paraderos = paraderos

    def to_dict(self) -> dict:
        return {
            "ruta_id": self.ruta_id,
            "fecha": self.fecha.isoformat(),
            "hora_inicio": self.hora_inicio.isoformat(),
            "hora_fin": self.hora_fin.isoformat(),
            "paraderos": [p.to_dict() for p in self.paraderos]
        }