import os
import PySimpleGUI as sg
import datetime as dt
from datetime import date, timedelta

dt_now = dt.datetime.now()
dt_next = dt_now + timedelta(days=1)
dt_nnext = dt_next + timedelta(days=1)
dt_nnnext = dt_nnext + timedelta(days=1)
dt_nnnnext = dt_nnnext + timedelta(days=1)

'''print(dt_now.year)

print(dt_now.month)

print(dt_now.day)

print(dt_now.strftime('%a'))


print(dt_next.year)

print(dt_next.month)

print(dt_next.day)

print(dt_next.strftime('%a'))


print(dt_nnext.year)

print(dt_nnext.month)

print(dt_nnext.day)

print(dt_nnext.strftime('%a'))


print(dt_nnnext.year)

print(dt_nnnext.month)

print(dt_nnnext.day)

print(dt_nnnext.strftime('%a'))


print(dt_nnnnext.year)

print(dt_nnnnext.month)

print(dt_nnnnext.day)

print(dt_nnnnext.strftime('%a'))'''

GetUp_file = 'GetUp_list.txt'

layout = [
    [sg.Text("起床時間")], 
    [sg.Multiline(size=(100, 15), key='output', disabled=True)]
]

win = sg.Window('起床時間設定アプリ', layout, font=(None, 14), size=(850, 500))

def load_getup():
    if os.path.exists(GetUp_file):
        with open(GetUp_file, 'r') as file:
            getup = file.readlines()
        getup = [review.strip() for review in getup if review.strip() != "------------------------------------------------------------------------"]
    else:
        getup = []
    return getup


win.close()