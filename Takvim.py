#!/usr/bin/env python
import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS takvim(
    islemgunu date, 
    islemsaat date, 
    OlayTipi text, 
    OlayAcikama text
)
""")
def takvimekle(Dat):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute("""INSERT INTO takvim("islemgunu", "islemsaat", "OlayTipi", "OlayAcikama") VALUES(?,?,?,?)""",Dat)
    conn.commit()
    c.fetchone()
    conn.close()

def takvimsorgula(islemtarih):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    search_command = """SELECT * from takvim WHERE islemgunu = '{}'  """
    c.execute(search_command.format(islemtarih))
    user = c.fetchone()
    conn.close
    return user

def takvimguncelle(Dat,islemtarihi):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    update_command = """UPDATE takvim SET islemgunu= '{}', islemsaat='{}',OlayTipi='{}', OlayAcikama='{}'  WHERE islemgunu = '{}'  """
    c.execute(update_command.format(Dat[0],Dat[1],Dat[2],Dat[3],islemtarihi))
    conn.commit()
    conn.close()

def takvimsil(islemtarihi):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    delete_command = """DELETE from takvim WHERE islemgunu = '{}'  """
    c.execute(delete_command.format(islemtarihi))
    conn.commit()
    conn.close()

sg.theme('Dark Red')
layout = [[sg.Text('Takvim', key='-TXT-')],
      [sg.Input(key='-SOR-', size=(20,1)), sg.CalendarButton('Sorgu İçin Tarih seç',  target='-SOR-', format='%d/%m/%Y', default_date_m_d_y=(6,12,2023), )], 
      [sg.Button('Sorgula'),sg.Button('Sil')],
      [sg.Text(size=(20,5),)],   
      [sg.Input(key='-IN-', size=(20,1)), sg.CalendarButton('Başlangıç günü seç',  target='-IN-', format='%d/%m/%Y', default_date_m_d_y=(6,12,2023), )],
      [sg.Input(key='-IN2-', size=(20,1)), sg.CalendarButton('Başlangıç saati seç',  target='-IN2-', format='%H:%M', default_date_m_d_y=(6,12,2023), )],
      [sg.Input(key='-IN3-', size=(20,1)), sg.Text(size=(20, 1), text="Olayın Tipi")],
      [sg.Input(key='-IN4-', size=(20,50)), sg.Text(size=(20, 1), text="Olayın Açıklanması")],
      [sg.Button('Ekle'),sg.Button('Güncelle'), sg.Exit()]]

window = sg.Window('window', layout)
Dat=[]
for i in range(4):
    Dat.append(i)
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Ekle':
        Dat[0]=values['-IN-']
        Dat[1]=values['-IN2-']
        Dat[2]=values['-IN3-']
        Dat[3]=values['-IN4-']
        takvimekle(Dat)
    elif event== 'Sorgula':
        sorgu=values['-SOR-']
        son=takvimsorgula(sorgu)
        print(son)
        sg.popup(son)
    elif event == 'Güncelle':
        sorgu=values['-SOR-']
        Dat[0]=values['-IN-']
        Dat[1]=values['-IN2-']
        Dat[2]=values['-IN3-']
        Dat[3]=values['-IN4-']
        takvimguncelle(Dat,sorgu)
    elif event =='Sil':
        sorgu=values['-SOR-']
        takvimsil(sorgu)
conn.commit()
c.close()
window.close()
    #c.execute('''INSERT INTO takvim("islembaslama", "islembitis", "OlayTipi", "OlayAcikama")
    #VALUES (?,?,?,?)''',(T1,T2,A1,A2))