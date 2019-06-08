from django.db import models

"""
[cpu]
name, nm, core(수치로 변환), thread, clock, l3, tdp, price
*core, l3
"""


class Cpu(models.Model):
    class Meta:
        app_label = "data"

    name = models.CharField(max_length=200)
    nm = models.IntegerField(default=0)
    core = models.IntegerField(default=0)
    thread = models.IntegerField(default=0)
    clock = models.FloatField(default=0)
    l3 = models.IntegerField(default=0)
    tdp = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


"""
[hdd]
name,capacity, rpm, buffer, thickness,price
*capacity
"""


class Hdd(models.Model):
    class Meta:
        app_label = "data"
    name = models.CharField(max_length=200)
    capacity = models.FloatField(default=0)
    rpm = models.IntegerField(default=0)
    buffer = models.IntegerField(default=0)
    thickness = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


"""
[mainboard]
name,chipset(범주), capacity,pcie_slot, sata3, price
*chipset
"""


class Mainboard(models.Model):
    class Meta:
        app_label = "data"
    name = models.CharField(max_length=200)
    chipset = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0)
    pcie_slot = models.IntegerField(default=0)
    sata3 = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


"""
[power]
name,w,a,4pin_ide,stata,6+2pin_pci-e,price
*w
"""


class Power(models.Model):
    class Meta:
        app_label = "data"
    name = models.CharField(max_length=200)
    w = models.IntegerField(default=0)
    a = models.IntegerField(default=0)
    pin4_ide = models.IntegerField(default=0)
    sata = models.IntegerField(default=0)
    pin6plus2_pci_e = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


"""
[ram]
name,manufacturer(범주), use(범주), dimm(범주), capacity,clock,price
*capacity,clock
"""


class Ram(models.Model):
    class Meta:
        app_label = "data"
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=50)
    use = models.CharField(max_length=50)
    dimm = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0)
    clock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


"""
[vga]
name,clock, b_clock, sp, gddr,memory_c,memory_v,memory_b,price
*clock,sp,memory_v
"""


class Vga(models.Model):
    class Meta:
        app_label = "data"
    name = models.CharField(max_length=200)
    clock = models.IntegerField(default=0)
    b_clock = models.IntegerField(default=0)
    sp = models.IntegerField(default=0)
    gddr = models.IntegerField(default=0)
    memory_c = models.IntegerField(default=0)
    memory_v = models.IntegerField(default=0)
    memory_b = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

