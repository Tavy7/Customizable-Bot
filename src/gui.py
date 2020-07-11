import PySimpleGUI as sg
import createBot
import runBot

sg.theme('DarkAmber')

layout = [ [sg.Button('Adauga bot', size=(13, 2))],
            [sg.Button('Ruleaza un bot', size=(13, 2))],
            [sg.Exit()] ]

window = sg.Window('Bot', layout)

while True:
    event, values = window.read()
    print(event, values)

    if event == 'Adauga bot':
        layoutInterogare = [ [sg.Text('Introduceti numele botului')],
                                [sg.InputText()],
                                [sg.Button('Ok')]]

        windowInterogare = sg.Window('Adauga Bot', layoutInterogare)

        while True:
            event, values = windowInterogare.read()
            if event == 'Ok':
                windowInterogare.close()
                createBot.main(values[0])
                break

    if event == 'Ruleaza un bot':
        runBot.main()

    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    
window.close()
