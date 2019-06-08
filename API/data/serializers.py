from rest_framework import serializers
from .models import Cpu
from .models import Hdd
from .models import Mainboard
from .models import Power
from .models import Ram
from .models import Vga

#col_name per item
col_name = {
'cpu' : ('name', 'nm', 'core', 'thread', 'clock', 'l3', 'tdp', 'price'),
'hdd' : ( 'name','capacity', 'rpm', 'buffer', 'thickness','price'),
'mainboard' : ('name','chipset', 'capacity', 'pcie_slot', 'sata3', 'price'),
'power' : ('name','w','a','pin4_ide','sata','pin6plus2_pci_e','price'),
'ram' : ('name','manufacturer', 'use', 'dimm', 'capacity','clock','price'),
'vga' : ('name','clock', 'b_clock', 'sp', 'gddr', 'memory_c', 'memory_v', 'memory_b','price')
}

class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = col_name['cpu']

class HddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hdd
        fields = col_name['hdd']

class MainboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainboard
        fields = col_name['mainboard']

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = col_name['power']

class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = col_name['ram']

class VgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vga
        fields = col_name['vga']