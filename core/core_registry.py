import uuid
import weakref

registries = {}

class Registry:
    def __init__(self, cls):
        registries[cls] = self
        self.cls = cls
        self.objects = weakref.WeakValueDictionary()

    def add(self, obj):
        if not isinstance(obj, self.cls):
            raise TypeError(f"Object must be of type {self.cls.__name__}")
        self.objects[obj.uuid] = obj

    def remove(self, obj):
        if obj.uuid in self.objects:
            del self.objects[obj.uuid]

    def get(self, uuid):
        if uuid in self.objects:
            return self.objects[uuid]
        else:
            return None

    def get_all(self):
        return self.objects.values()

    def get_all_uuids(self):
        return self.objects.keys()

    def __iter__(self):
        return iter(self.objects.values())

    def __len__(self):
        return len(self.objects)

    def __contains__(self, item):
        return item in self.objects.values()

    @classmethod
    def register(cls, to_register):

        registry = cls(to_register)
        to_register.registry = registry

        def wrapper(func):
            def wrapper_new(*args, **kwargs):
                obj = func(*args, **kwargs)
                obj.uuid = uuid.uuid4()
                registry.add(obj)
                return obj
            return wrapper_new
        to_register.__new__ = wrapper(to_register.__new__)

        return to_register

