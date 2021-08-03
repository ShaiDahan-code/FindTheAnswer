import PySimpleGUI as sg
import SearchAlgoritem

layout = [  [sg.Text('Question:                          '), sg.Input(key='Question')],
            [sg.Text('Possible answer number 1: '), sg.Input(key='Answer1')],
            [sg.Text('Possible answer number 2: '), sg.Input(key='Answer2')],
            [sg.Text('Possible answer number 3: '), sg.Input(key='Answer3')],
            [sg.Text('Possible answer number 4: '), sg.Input(key='Answer4')],
            [sg.Text("Answer is: "), sg.Text(size=(40, 1), key='-OUTPUT-')],
            [sg.Button('Search Answer'), sg.Button('Clear'),sg.Button('Quit')]
]
window = sg.Window('Find The Answer', layout)
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Clear':
        window['Question'].update("")
        window['Answer1'].update("")
        window['Answer2'].update("")
        window['Answer3'].update("")
        window['Answer4'].update("")
        window['-OUTPUT-'].update("")

    if event == 'Search Answer':
        p1 = SearchAlgoritem.Search(values['Question'], values['Answer1'], values['Answer2'], values['Answer3'], values['Answer4'])
        p1.searchAnswer()
        p1.countTheAnswer()
        window['-OUTPUT-'].update(f"The most poosible answer is: {p1.getAnswer()}")


window.close()

# p1 = sa.Search("הבן אדם המבוגר בעולם","אביחי עזיז","ז'אן לואיז קלמן","שראל אלוש","אסף בן שבת")
# p1.searchAnswer()
# p1.countTheAnswer()
# p1.getAnswer()
