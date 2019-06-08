from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from .views import PowerViewSet
from .views import VgaViewSet
from .views import CpuViewSet
from .views import HddViewSet
from .views import RamViewSet
from .views import MainboardViewSet

router = routers.DefaultRouter()

router.register('power', PowerViewSet)
router.register('vga', VgaViewSet)
router.register('cpu', CpuViewSet)
router.register('hdd', HddViewSet)
router.register('ram', RamViewSet)
router.register('mainboard', MainboardViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
