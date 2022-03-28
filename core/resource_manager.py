import sys


class Registry:
    def __init__(self, cls):
        self.registered_class = cls
        self.resources = {}

    def register(self, name, resource):
        if issubclass(self.registered_class, resource.__class__):
            self.resources[name] = resource

    def get(self, name):
        return self.resources[name]



class ResourceManager:
    __instance__ = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance__:
            cls.__instance__ = super(ResourceManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance__

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __init__(self):
        self.registries = {}


class ResourceManagerError(Exception):
    def __init__(self, message):
        frame = sys._getframe(1)
        function = frame.f_code
        file_name = function.co_filename
        prev_frame = frame.f_back
        prev = prev_frame.f_code

        out = f"""
        {prev.co_filename}:{prev_frame.f_lineno} {prev.co_name} -> 
          {file_name}: {function.co_firstlineno} -> 
            {function.co_name}{function.co_varnames}:
              {file_name}: {frame.f_lineno} -> [{message}]
        """

        super().__init__(out)

    def __str__(self):
        return self.message