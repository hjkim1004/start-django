# 학습시킬 데이터를 전처리하기 위한 파일
# NA 처리만 하고, 범주형 데이터는 처리하지 않는다.
# 범주형 데이터는 학습할 때 처리

from API.data.crawled_data import frames
import pandas as pd

import re
p = re.compile(r'\d+GB|\d+TB') # 용량 추출

# 데이터 프레임 받아오기
ml = frames.get_frames("ml")

""" cpu 정제 """
cpu = ml['cpu']
frames.fillna_frequent(cpu,'nm')
substr = ['듀얼','트리','쿼드','헥사','옥타']; newSubStr=[2,3,4,6,8]
cpu['core'] = cpu['core'].replace(substr,newSubStr)


"""
hdd 정제
"""
hdd = ml['hdd']
capa_str = []; capa_mode = []; capa_int = [] #용량 새로 지정
for name in hdd['name']:
    list = name.split()
    for l in list:
        if p.search(l) != None:
            capa_str.append(p.search(l).group(0))
# GB인지 TB인지 검사하는 mode
for i in capa_str:
        capa_mode.append(i[-2] + i[-1])
# Capacity 숫자
for x in range(len(capa_str)):
    if capa_mode[x] == "GB":
        capa_int.append(float(capa_str[x][:-2]) * 0.001)
    elif capa_mode[x] == "TB":
        capa_int.append(capa_str[x][:-2])
# 최빈값 대체
frames.fillna_frequent(hdd,'buffer')

""" mainboard 정제 """
mainboard = ml['mainboard']
frames.fillna_frequent(mainboard,'pcie_slot')
frames.fillna_frequent(mainboard,'capacity')
frames.fillna_frequent(mainboard,'sata3')

""" power """
power = ml["power"]
for col in power.columns:
    frames.fillna_frequent(power,col)

""" ram """
ram = ml["ram"]
frames.fillna_frequent(ram,'use')
frames.fillna_frequent(ram, 'dimm')

""" vga """
vga = ml["vga"]
vga = vga.dropna()


def get_frames():
    return ml

