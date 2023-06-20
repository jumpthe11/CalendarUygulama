#!/usr/bin/env python
import PySimpleGUI as sg
import sqlite3

sg.theme('Dark Red')
layout = [[sg.Text('Date Chooser Test Harness', key='-TXT-')],
      [sg.Input(key='-IN-', size=(20,1)), sg.CalendarButton('Başlangıç tarihi seç',  target='-IN-', format='%d/%m/%Y %H:%M', default_date_m_d_y=(12,6,2023), )],
      [sg.Input(key='-IN2-', size=(20,1)), sg.CalendarButton('Bitiş tarihi seç',  target='-IN2-', format='%d/%m/%Y %H:%M', default_date_m_d_y=(12,6,2023), )],
      [sg.Input(key='-IN3-', size=(20,1)), ],
      [sg.Input(key='-IN4-', size=(20,1)), ],
      [sg.Button('Seç'), sg.Exit()]]

window = sg.Window('window', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Seç':
        print(values['-IN4-'])
window.close()