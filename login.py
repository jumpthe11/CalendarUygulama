import PySimpleGUI as sg
import sqlite3
from Register import *
conn = sqlite3.connect('Database.db')
c = conn.cursor()


layout = [[sg.Text('Kullanıcı Adı:'),  sg.Input(key='Kullanıcı')],
          [sg.Text('Parola:'),  sg.Input(key='Password')],
          [sg.Button('Giriş yap'), sg.Button('Çık')]]
window = sg.Window('Window Title', layout)
Datas=[]
for i in range(1):
    Datas.append(i)
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Çık':
        break
    if event == 'Giriş yap':
        search = searchKullaniciad(Datas[0])
        if search == None:
            print("Böyle kullanıcı yok")
            continue



conn.close()
window.close()