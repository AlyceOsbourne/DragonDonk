class AssetManager:
    
    assets_path: str
    plugins_path: str
    
    __instance__: "AssetManager" = None
    
    def __new__(cls):
        if not cls.__instance__:
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__

    @classmethod
    def invoke(cls, func):
        def wrapper(*args, **kwargs):
            return func(AssetManager(), 
                        *args, 
                        **kwargs)
        return wrapper
            

            