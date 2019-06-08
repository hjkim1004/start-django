from django.db import models

# Create your models here.

class Cpu(models.Model):
    #    colName = ['name', 'manufacturer', 'socket', 'nm', 'core', 'thread', 'clock',
    #              'l2', 'l3', 'bit', 'tdp', 'gpu_name', 'gpu_core', 'etc', 'img', 'price']

    name = models.CharField(max_length=300)
    manufacturer = models.CharField(max_length=10)
    socket = models.CharField(max_length=20)
    nm = models.IntegerField()
    core = models.CharField(max_length=5)
    thread = models.IntegerField()
    clock = models.FloatField()
    l2 = models.IntegerField()
    l3 = models.IntegerField()
    bit = models.CharField(max_length=10)
    tdp = models.IntegerField()
    gpu_name = models.CharField(max_length=100)
    gpu_core = models.IntegerField()
    etc = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Hdd(models.Model):

    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=10)
    type = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    capacity = models.CharField(max_length=10)
    sata = models.CharField(max_length=20)
    rpm = models.IntegerField()
    buffer = models.IntegerField()
    width = models.IntegerField()
    thickness = models.CharField(max_length=20)
    noise = models.IntegerField()
    etc = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Mainboard(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=20)
    socket = models.CharField(max_length=20)
    chipset = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    phase = models.IntegerField()
    ddr = models.IntegerField()
    capacity = models.IntegerField()
    vga_connect = models.IntegerField()
    pcie_slot = models.IntegerField()
    sata3 = models.IntegerField()
    m_2_slot = models.IntegerField()
    output = models.IntegerField()
    ps_2 = models.IntegerField()
    usb_2_0 = models.IntegerField()
    usb_3_1_1 = models.IntegerField()
    usb_3_1_2 = models.IntegerField()
    etc = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Power(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=20)
    standard = models.CharField(max_length=10)
    w = models.IntegerField()
    fan_size = models.IntegerField()
    fan_num = models.IntegerField()
    pfc = models.CharField(max_length=10)
    rail = models.CharField(max_length=10)
    a = models.IntegerField()
    pin4_ide = models.IntegerField() #4pin_ide
    sata = models.IntegerField()
    pin6plus2_pci_e = models.IntegerField() # 6+2pin_pci-e
    as_power = models.IntegerField() # as
    etc = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Ram(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=20)
    ddr = models.IntegerField()
    use = models.CharField(max_length=10)
    count = models.IntegerField()
    heatsink = models.CharField(max_length=10)
    dimm = models.CharField(max_length=10)
    capacity = models.IntegerField()
    clock = models.IntegerField()
    etc = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Vga(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=20)
    prod_name = models.CharField(max_length=15)
    nm = models.IntegerField()
    clock = models.IntegerField()
    b_clock= models.IntegerField()
    sp = models.IntegerField()
    PCIe = models.CharField(max_length=10)
    gddr = models.IntegerField()
    memory_c=models.IntegerField()
    memory_v = models.IntegerField()
    memory_b = models.IntegerField()
    etc = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name
