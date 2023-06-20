import PySimpleGUI as sg
import sys
import sqlite3
conn = sqlite3.connect('Database.db')
c = conn.cursor()
#Tablo yok ise yeni bir tablo oluşturur
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
layout = [[sg.Text('Giriş ekranı:'), sg.Button('Giriş')],
          [sg.Text('Kayıt ekranı:'), sg.Button('Kayıt')],
          [sg.Text('ÇIKIŞ'), sg.Button('ÇIK')]
          
          ]

window = sg.Window('Ana menü hoş geldiniz', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event =='ÇIK':
        break
    if event == 'Giriş':
        execfile('login.py')
    if event == 'Kayıt':
        execfile('Register.py')
conn.close()
window.close()