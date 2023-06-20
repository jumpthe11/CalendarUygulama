import PySimpleGUI as sg
import sqlite3
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

layout = [[sg.Text('Ad:'),  sg.Input(key='Ad')],
          [sg.Text('Soyad:'),  sg.Input(key='Soyad')],
          [sg.Text('Kullanıcı Adı:'),  sg.Input(key='Kullanıcı')],
          [sg.Text('Parola:'),  sg.Input(key='Password')],
          [sg.Text('TC Kimlik No:'),  sg.Input(key='TC')],
          [sg.Text('Telefon:'),sg.Input(key='Telefon')],
          [sg.Text('Email:'),  sg.Input(key='Email')],
          [sg.Text('Adres:'),  sg.Input(key='Adres')],
          [sg.Text('KullanıcıType:'),  sg.Input(key='KullanıcıType')],
          [sg.Button('Kaydol'), sg.Button('Çık')]]

window = sg.Window('Window Title', layout)
Aas=[]
for i in range(9):
    Aas.append(i)
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Çık':
        break
    if event == 'Kaydol':
        Aas[0]=values['Ad']
        Aas[1]=values['Soyad']
        Aas[2]=values['Kullanıcı']
        Aas[3]=values['Password']
        Aas[4]=values['TC']
        Aas[5]=values['Telefon']
        Aas[6]=values['Email']
        Aas[7]=values['Adres']
        Aas[8]=values['KullanıcıType']
        c.execute("""INSERT INTO kullanici("Ad", "Soyad", "Kullanıcı", "Password", "TC", "Telefon", "Email", "Adres", "KullanıcıType")
          VALUES (?,?,?,?,?,?,?,?,?)""",Aas
          )

        conn.commit()
conn.close()
window.close()

#        c.execute("""INSERT INTO kullanici VALUES ("Ad", "Soyad ", "Kullanıcı ", "Password ", "TC ", "Telefon ", "Email ", "Adres ", "KullanıcıType ")""")
#        c.execute('''INSERT INTO kullanici("Ad", "Soyad", "Kullanıcı", "Password", "TC", "Telefon", "Email", "Adres", "KullanıcıType")
#          VALUES ('Ad','Soyad','Kad','Parola','TCNO','Telefon','Email','Adres','Ktype')
#          ''')