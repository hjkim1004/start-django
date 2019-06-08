from django.contrib import admin
from .models import Vga
from .models import Cpu
from .models import Ram
from .models import Power
from .models import Mainboard
from .models import Hdd
# Register your models here.

admin.site.register(Vga)
admin.site.register(Cpu)
admin.site.register(Ram)
admin.site.register(Power)
admin.site.register(Mainboard)
admin.site.register(Hdd)




