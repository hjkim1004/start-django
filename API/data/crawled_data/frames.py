# Frame 관련 함수
# CSV 파일을 pandas의 데이터 프레임으로 저장하여 데이터 정제하기

import os
import glob
import pandas as pd
from API.API.settings import BASE_DIR

#path 지정
path = BASE_DIR + "/data/crawled_data/"

contents = ['cpu','hdd','mainboard','power','ram','vga'] #contents item
paths = { c : path + c for c in contents} #col_names => _contents_col_names format
col_paths = {c : paths[c]+'/_'+c+'_col_names.txt' for c in contents}

frames = {}
ml = {}

ml_col_name = {
    'cpu': ('name', 'nm', 'core', 'thread', 'clock', 'l3', 'tdp', 'price'),
    'hdd': ('name','capacity', 'rpm', 'buffer', 'thickness','price'),
    'mainboard': ('name', 'chipset', 'capacity', 'pcie_slot', 'sata3', 'price'),
    'power': ('name', 'w', 'a', 'pin4_ide', 'sata', 'pin6plus2_pci_e','price'),
    'ram': ('name','manufacturer', 'use', 'dimm', 'capacity','clock','price'),
    'vga': ('name','clock', 'b_clock', 'sp', 'gddr', 'memory_c', 'memory_v', 'memory_b','price')
}

def read_col_name(c):
    with open(col_paths[c]) as f:
        line = f.readline()
        return line.strip().split(',')

col_names = {c : read_col_name(c) for c in contents} # column name

def make_frame(c):
    pieces = []
    for files in glob.glob(os.path.join(paths[c],'*.csv')):
        frame = pd.read_csv(files, names = col_names[c], header = None)
        pieces.append(frame)
    c = pd.concat(pieces,ignore_index=True)
    return c

for c in contents:
    frames[c] = make_frame(c)
    frames[c] = frames[c].loc[frames[c]['price'].notnull()]  # remove rows when price value is null
    frames[c] = frames[c].drop_duplicates().reset_index(drop=True)  # remove duplicated rows
    ml[c] = frames[c].loc[:, ml_col_name[c]]

def get_frames(mode):
    if mode == "concat":
        return frames
    elif mode == "ml":
        return ml

# 최빈값으로 대체하는 함수
def fillna_frequent(frame, col):
    frame[col] = frame[col].fillna(frame[col].value_counts().idxmax())

# 번주형 데이터 처리하기
def one_hot_encoding(frame, columns):
    frame_columns = pd.get_dummies(frame,columns=columns)
    frame = pd.concat([frame, frame_columns],axis=1)
    return frame
