class NotFoundException(Exception):
    def __init__(self, detail: str):
        self.detail = detail


class ValidationException(Exception):
    def __init__(self, detail: str):
        self.detail = detail


class ConflictException(Exception):
    def __init__(self, detail: str):
        self.detail = detail