class Vga:
    """
    VGA

    Singleton Pattern
    """
    colName = ['name', 'manufacturer', 'prod_name', 'nm', 'clock', 'b_clock',
             'sp', 'PCIe', 'gddr', 'memory_c', 'memory_v', 'memory_b', 'img', 'etc', 'price']
    colIdentifier = ['nm', '', '', '개', '', 'GDDR', 'MHz', 'GB', '-bit', '', 'http']
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