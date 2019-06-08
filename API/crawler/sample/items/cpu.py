class Cpu:
    """
    CPU

    Singleton pattern
    """
    colName = ['name', 'manufacturer', 'socket', 'nm', 'core', 'thread', 'clock',
                  'l2', 'l3', 'bit', 'tdp', 'gpu_name', 'gpu_core', 'img', 'etc', 'price']
    colIdentifier = ['', 'nm', '코어', '개', 'GHz', 'B', 'B', '비트', 'W',
                     ['인텔', 'AMD'], 'MHz', 'http']

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