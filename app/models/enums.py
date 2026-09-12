from enum import Enum

class TipoServicio(str, Enum):
    METROPOLITANO = "metropolitano"
    CORREDOR_ROJO = "corredor_rojo"
    CORREDOR_AZUL = "corredor_azul"
    CORREDOR_MORADO = "corredor_morado"
    CORREDOR_ROSADO = "corredor_rosado"

class Sentido(str, Enum):
    IDA = "IDA"
    VUELTA = "VUELTA"