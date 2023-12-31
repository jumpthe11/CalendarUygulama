import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()

#İki farklı yerde oluşturma kodu olması gerekmiyordu. Sadece anamenüden başlatılsa yeterli.
'''
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
'''
def searchKullaniciad(kullaniciad):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    search_command = """SELECT * from kullanici WHERE Kullanıcı = '{}'  """
    c.execute(search_command.format(kullaniciad))
    user = c.fetchone()
    conn.close
    return user

def searchLogin(kullanici,Sifre):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    search_command = """SELECT * from kullanici WHERE Kullanıcı = '{}' AND Password = '{}'  """
    c.execute(search_command.format(kullanici,Sifre))
    sifredurum = c.fetchone()
    conn.close
    return sifredurum

if __name__=="__main__":
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
            search=searchKullaniciad(Aas[2])
            if search != None:
                print("Kullanıcı adı mevcut")
                window.close()
            c.execute('''INSERT INTO kullanici("Ad", "Soyad", "Kullanıcı", "Password", "TC", "Telefon", "Email", "Adres", "KullanıcıType")
          VALUES (?,?,?,?,?,?,?,?,?)''',Aas)
    conn.commit()
    conn.close()
    window.close()

#        c.execute("""INSERT INTO kullanici VALUES ("Ad", "Soyad ", "Kullanıcı ", "Password ", "TC ", "Telefon ", "Email ", "Adres ", "KullanıcıType ")""")
#        c.execute('''INSERT INTO kullanici("Ad", "Soyad", "Kullanıcı", "Password", "TC", "Telefon", "Email", "Adres", "KullanıcıType")
#          VALUES ('Ad','Soyad','Kad','Parola','TCNO','Telefon','Email','Adres','Ktype')
#          ''')