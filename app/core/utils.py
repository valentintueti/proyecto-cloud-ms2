import uuid


def generar_id(prefijo: str) -> str:
    return f"{prefijo}_{uuid.uuid4().hex[:8]}"


def documento_a_dict(doc: dict) -> dict:
    if doc is None:
        return None
    doc = dict(doc)
    doc["id"] = doc.pop("_id")
    return doc