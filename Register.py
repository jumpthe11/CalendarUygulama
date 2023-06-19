import PySimpleGUI as sg
import sqlite3
conn = sqlite3.connect('Database.db')
c = conn.cursor()

'''
c.execute("""CREATE TABLE kullanici(
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

'''
conn.commit()
layout = [[sg.Text('Ad:'),  sg.Input(key='Ad')],
          [sg.Text('Soyad:'),  sg.Input(key='Soyad')],
          [sg.Text('Kullanıcı Adı:'),  sg.Input(key='K_ad')],
          [sg.Text('Parola:'),  sg.Input(key='Password')],
          [sg.Text('TC Kimlik No:'),  sg.Input(key='TCNO')],
          [sg.Text('Telefon:'),sg.Input(key='Telefon')],
          [sg.Text('Email:'),  sg.Input(key='Email')],
          [sg.Text('KullanıcıType:'),  sg.Input(key='Type')],
          [sg.Button('Kaydol'), sg.Button('Çık')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Çık':
        break
    if event == 'Kaydol':
        degerler=values['Ad']
        c.execute("INSERT INTO kullanici")
        print(degerler)
conn.close()
window.close()
