class Ram:
    """
    Ram

    Singleton Pattern
    """
    colName = ['name', 'manufacturer', 'ddr', 'use', 'count', 'heatsink',
               'dimm', 'capacity', 'clock', 'img', 'etc', 'price']
    colIdentifier = ['DDR', '용', 'ea', '포함', 'Dimm', 'GB', 'MHz', 'http']
    _instance = None

    @classmethod
    def _get_instance(cls):
        return cls._instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._get_instance
        return cls._instance

    def __init__(self):
        self._dict = {col: "NA" for col in self.colName}

