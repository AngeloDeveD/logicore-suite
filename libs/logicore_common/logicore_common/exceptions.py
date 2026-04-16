class LogiCoreException(Exception):
    """Базовое исключение для всей платформы"""
    pass

class EntityNotFoundException(LogiCoreException):
    """Выбрасывается, если объект не найден в любой БД"""
    def __init__(self, entity_name: str, entity_id: any):
        self.message = f"{entity_name} with id {entity_id} not found."
        super().__init__(self.message)