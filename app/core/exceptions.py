class NotFoundException(Exception):
    """Se lanza cuando un recurso (ruta, servicio, paradero) no existe."""
    def __init__(self, detail: str):
        self.detail = detail


class ValidationException(Exception):
    """Se lanza cuando una regla de negocio no se cumple
    (ej. ruta_id no existe al crear un servicio)."""
    def __init__(self, detail: str):
        self.detail = detail


class ConflictException(Exception):
    """Se lanza cuando se intenta crear un recurso que ya existe (id duplicado)."""
    def __init__(self, detail: str):
        self.detail = detail