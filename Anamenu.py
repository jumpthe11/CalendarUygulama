import PySimpleGUI as sg
import sys
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
window.close()