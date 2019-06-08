"""
model_instance = Post(author=User.objects.all()[0], title='title', text='content')
model_instance.save()
"""
import os
from django.conf import settings
from API.API.settings import BASE_DIR
import django

settings.configure(Debug=True)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API.settings')
django.setup()

import API.data.preprocessing as pp
from API.data.models import Vga
from API.data.models import Mainboard
from API.data.models import Ram
from API.data.models import Power
from API.data.models import Cpu
from API.data.models import Hdd


frame = pp.get_frames()

content = ['cpu','hdd','mainboard','ram','power','vga']
for c in content:
    for index, row in frame[c].iterrows():
        col = frame[c].columns
        kwargs = {c: row[c] for c in col}
        if c == "cpu": model = Cpu(**kwargs)
        elif c == "hdd": model = Hdd(**kwargs)
        elif c == "mainboard": model = Mainboard(**kwargs)
        elif c == "ram": model = Ram(**kwargs)
        elif c == "power": model = Power(**kwargs)
        elif c == "vga": model = Vga(**kwargs)
        model.save()