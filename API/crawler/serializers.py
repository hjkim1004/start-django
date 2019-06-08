from rest_framework import serializers
from .models import Cpu
from .models import Hdd
from .models import Mainboard
from .models import Power
from .models import Ram
from .models import Vga

#col_name per item
col_name = {'cpu': ('name','manufacturer','socket','nm','core','thread','clock','l2','l3',
                    'bit','tdp','gpu_name','gpu_core','etc','price'),
 'hdd': ('name','manufacturer','type','size','capacity','sata','rpm',
         'buffer','width','thickness','noise','etc','price'),
 'mainboard': ('name','manufacturer','socket','chipset','size','phase',
               'ddr','capacity','vga_connect','pcie_slot','sata3','m_2_slot',
               'output','ps_2','usb_2_0','usb_3_1_1','usb_3_1_2','etc','price'),
 'power': ('name','manufacturer','standard','w','fan_size','fan_num',
           'pfc','rail','a','pin4_ide','sata','pin6plus2_pci_e','as_power','etc','price'),
 'ram': ('name','manufacturer','ddr','use','count','heatsink','dimm','capacity','clock','etc','price'),
 'vga': ('name','manufacturer','prod_name','nm','clock','b_clock','sp','PCIe','gddr',
         'memory_c','memory_v','memory_b','etc','price')}

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