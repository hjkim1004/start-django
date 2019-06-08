class Hdd:
    """
    Hdd

    Singleton pattern
    """

    colName = ['name', 'manufacturer', 'type', 'size', 'capacity', 'sata', 'rpm', 'buffer',
                'thickness', 'noise', 'as', 'img', 'etc', 'price']
    colIdentifier = ['', '', '', '', 'B', 'b/s', 'RPM', '메모리', '두께:', '소음(유휴/탐색):', '년','http']

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