
__all__ = []

def __export__(definition):
    globals()[definition.__name__] = definition
    __all__.append(definition.__name__)
    return definition


@__export__
class ResourceManager:
    __instance__ = None

    __map_registry__ = {}
    __quest_registry__ = {}

    __actor_registries__ = {
        "creatures": {},
        "npcs": {},
        "players": {}
    }

    __item_registries__ = {
        "item": {},
        "weapon": {},
        "armor": {},
        "potion": {},
        "scroll": {},
        "key": {},
        "food": {},
        "misc": {}
    }

    def __new__(cls, *args, **kwargs):
        if not cls.__instance__:
            cls.__instance__ = super(ResourceManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__

    def __init__(self):
        pass




print(__all__)