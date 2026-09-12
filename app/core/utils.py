import uuid


def generar_id(prefijo: str) -> str:
    """Genera un id legible tipo 'srv_3f9a2b1c' en vez de un ObjectId de Mongo,
    manteniendo la consistencia con los ids de ejemplo (R001, srv_001, par_002)."""
    return f"{prefijo}_{uuid.uuid4().hex[:8]}"


def documento_a_dict(doc: dict) -> dict:
    """Convierte el campo _id de Mongo a 'id' para que coincida con los schemas de respuesta."""
    if doc is None:
        return None
    doc = dict(doc)
    doc["id"] = doc.pop("_id")
    return doc