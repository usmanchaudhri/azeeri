class ObjectFactory:
    def __init__(self):
        self.builder = {}

    def register_builder(self, key, builder):
        self.builder[key] = builder

    def create(self, key, **kwargs):
        builder = self.builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)

