import PySimpleGUI as sg
import sqlite3
from Register import *
conn = sqlite3.connect('Database.db')
c = conn.cursor()


layout = [[sg.Text('Kullanıcı Adı:'),sg.Input(key='Kullanıcı')],
          [sg.Text('Parola:'),  sg.Input(key='Password')],
          [sg.Button('Giriş yap'), sg.Button('Çık')]]

window = sg.Window('Window Title', layout)
Datas=[]
for i in range(2):
    Datas.append(i)

while True:
    event, values = window.read()
    print(event, values)
    Datas[0]=values['Kullanıcı']
    Datas[1]=values['Password']
    if event == sg.WIN_CLOSED or event == 'Çık':
        break
    if event == 'Giriş yap':
        search = searchKullaniciad(Datas[0])
        if search != None:
            print("Böyle kullanıcı Var")
            continue
        logindurum = searchLogin(Datas[0],Datas[1])
        if logindurum != None:
            print("oldu")
            execfile(Takvim.py)




conn.close()
window.close()