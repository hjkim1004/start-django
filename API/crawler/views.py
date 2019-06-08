from django.shortcuts import render
from rest_framework import viewsets

from .models import Power
from .models import Mainboard
from .models import Ram
from .models import Cpu
from .models import Hdd
from .models import Vga

from .serializers import PowerSerializer
from .serializers import MainboardSerializer
from .serializers import RamSerializer
from .serializers import CpuSerializer
from .serializers import HddSerializer
from .serializers import VgaSerializer

# Create your views here.

class PowerViewSet(viewsets.ModelViewSet):
    queryset = Power.objects.all()
    serializer_class = PowerSerializer

class MainboardViewSet(viewsets.ModelViewSet):
    queryset = Mainboard.objects.all()
    serializer_class = MainboardSerializer

class RamViewSet(viewsets.ModelViewSet):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer

class CpuViewSet(viewsets.ModelViewSet):
    queryset = Cpu.objects.all()
    serializer_class = CpuSerializer

class HddViewSet(viewsets.ModelViewSet):
    queryset = Hdd.objects.all()
    serializer_class = HddSerializer

class VgaViewSet(viewsets.ModelViewSet):
    queryset = Vga.objects.all()
    serializer_class = VgaSerializer



