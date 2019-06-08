class Mainboard:
    """
    Mainboard

    Singleton pattern
    """

    colName = ['name', 'manufacturer', 'socket', 'chipset', 'size', 'phase',
                'ddr', 'capacity', 'vga_connect', 'pcie_slot', 'sata3', 'm_2_slot',
                'output', 'ps_2', 'usb_2_0', 'usb_3_1_1', 'usb_3_1_2', 'img', 'etc', 'price']
    colIdentifier = ['cm', '페이즈', 'DDR', 'GB', 'VGA 연결: ', 'PCIe 슬롯: ', 'SATA3: ',
                 'M.2 슬롯: ', 'ch', 'PS/2: ', 'USB 2.0: ', 'USB 3.1 Gen 1: ', 'USB 3.1 Gen 2: ','http']
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