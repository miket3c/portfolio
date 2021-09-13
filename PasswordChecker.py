import PySimpleGUI as sg

sg.theme('DarkGrey 13')

layout = [[sg.Text('Please enter your password:'), sg.Text(size=(18,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Submit'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout, size=(400,100))
pass_test = 0
while True:  
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Submit':
        window['-OUTPUT-'].update(values['-IN-'])
        if values["-IN-"] == "password":
            window["-OUTPUT-"].update("Success!")
            pass_test = 1
            break
        else: 
            window["-OUTPUT-"].update("Incorrect. Try again.")

window.close()

layout2 = [[sg.Text("You successfully entered your password!")], [sg.Button("OK")]]

if pass_test == 1:
    window2 = sg.Window("Success!", layout2)

    while True:
        event, values = window2.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window2.close()