import PySimpleGUI as sg
import sqlite3
from Register import *
conn = sqlite3.connect('Database.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS kullanici(
    Ad text, 
    Soyad text, 
    Kullanıcı Adı text, 
    Password text, 
    TC Kimlik No text, 
    Telefon text, 
    Email text,
    Adres text,
    KullanıcıType text
)
""")

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

    if event == sg.WIN_CLOSED or event == 'Çık':
        break
    if event == 'Giriş yap':
        Datas[0]=values['Kullanıcı']
        Datas[1]=values['Password']
        search = searchKullaniciad(Datas[0])
        if search == None:
            sg.popup("Böyle kullanıcı yok")
            continue
        logindurum = searchLogin(Datas[0],Datas[1])
        if logindurum != None:
            execfile('Takvim.py')




conn.close()
window.close()