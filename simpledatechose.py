import PySimpleGUI as sg
layout = [[sg.Text('Date Chooser Test Harness', key='-TXT-')],
[sg.Button('Date Popup'), sg.Exit()]]
window = sg.Window('window', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Date Popup':
        sg.popup('You chose:', sg.popup_get_date())
window.close()