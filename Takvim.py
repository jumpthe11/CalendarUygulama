#!/usr/bin/env python
import PySimpleGUI as sg
import sqlite3

conn = sqlite3.connect('Database.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS takvim(
    islembaslama date, 
    islembitis date, 
    OlayTipi text, 
    OlayAcikama text
)
""")
def takvimekle(Dat):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute("""INSERT INTO takvim("islembaslama", "islembitis", "OlayTipi", "OlayAcikama") VALUES(?,?,?,?)""",Dat)
    conn.commit()
    c.fetchone()
    conn.close()

sg.theme('Dark Red')
layout = [[sg.Text('Takvim', key='-TXT-')],
      [sg.Input(key='-IN-', size=(20,1)), sg.CalendarButton('Başlangıç tarihi seç',  target='-IN-', format='%d/%m/%Y %H:%M', default_date_m_d_y=(12,6,2023), )],
      [sg.Input(key='-IN2-', size=(20,1)), sg.CalendarButton('Bitiş tarihi seç',  target='-IN2-', format='%d/%m/%Y %H:%M', default_date_m_d_y=(12,6,2023), )],
      [sg.Input(key='-IN3-', size=(20,1)), sg.Text(size=(20, 1), text="Olayın Tipi")],
      [sg.Input(key='-IN4-', size=(20,50)), sg.Text(size=(20, 1), text="Olayın Açıklanması")],
      [sg.Button('Seç'), sg.Exit()]]

window = sg.Window('window', layout)
Dat=[]
for i in range(4):
    Dat.append(i)
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Seç':
        Dat[0]=values['-IN-']
        Dat[1]=values['-IN2-']
        Dat[2]=values['-IN3-']
        Dat[3]=values['-IN4-']
        takvimekle(Dat)
conn.commit()
c.close()
window.close()
    #c.execute('''INSERT INTO takvim("islembaslama", "islembitis", "OlayTipi", "OlayAcikama")
    #VALUES (?,?,?,?)''',(T1,T2,A1,A2))