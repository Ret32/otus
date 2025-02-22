class LowFuelError(Exception):
    """Ошибка: недостаточно топлива"""
    pass

class NotEnoughFuel(Exception):
    """Ошибка: топливо закончилось во время движения"""
    pass

class CargoOverload(Exception):
    """Ошибка: превышен грузоподъемный лимит"""
    pass