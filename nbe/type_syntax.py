class Basic:
    def __init__(self, identifier):
        self.identifier = identifier


class Arrow:
    def __init__(self, source, target):
        self.source = source
        self.target = target


class Product:
    def __init__(self, first, second):
        self.first = first
        self.second = second