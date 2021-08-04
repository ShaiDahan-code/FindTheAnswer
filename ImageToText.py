import pytesseract
import PySimpleGUI as sg
import SearchAlgoritem
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

file_types = [  ("JPEG (*.jpeg)", "*.jpeg"),
                ("JPEG (*.jpg)", "*.jpg"),
                ("All files (*.*)", "*.*")
                                            ]
class ImageToTextConvert:
    def __init__(self):
        self.QandAnswerLST = []
        layoutPhoto = [[sg.Text('Upload photo here: '), sg.Input(size=(25, 1), key='-PHOTO-'), sg.FileBrowse(file_types=file_types), sg.Button("Load Image")],
                       [sg.Text("Question: "), sg.Input(key="Q", size=(65, 1))],
                       [sg.Text("Answer 1: "), sg.Input(key="A1", size=(65, 1))],
                       [sg.Text("Answer 2: "), sg.Input(key="A2", size=(65, 1))],
                       [sg.Text("Answer 3: "), sg.Input(key="A3", size=(65, 1))],
                       [sg.Text("Answer 4: "), sg.Input(key="A4", size=(65, 1))],

                       [sg.Button('Send'), sg.Button("Update")]
                       ]
        windowPhoto = sg.Window('Find The Answer -Photo', layoutPhoto)
        while True:
            eventPhoto, valuesPhoto = windowPhoto.read()
            if eventPhoto == sg.WINDOW_CLOSED or eventPhoto == 'Send':
                break
            if eventPhoto == "Load Image":
                print(valuesPhoto['-PHOTO-'])
                img = Image.open(valuesPhoto['-PHOTO-'])
                print(pytesseract.image_to_string(img))
                text = pytesseract.image_to_string(img).split('\n')
                for sentence in text:
                    if sentence != ' ' and sentence != '':
                        sentence = sentence[2:]
                        self.QandAnswerLST.append(sentence)

                print(self.QandAnswerLST[:-1])
                windowPhoto['Q'].update(self.QandAnswerLST[0])
                windowPhoto['A1'].update(self.QandAnswerLST[1])
                windowPhoto['A2'].update(self.QandAnswerLST[2])
                windowPhoto['A3'].update(self.QandAnswerLST[3])
                windowPhoto['A4'].update(self.QandAnswerLST[4])
            if eventPhoto == 'Update':
                self.QandAnswerLST[0] = valuesPhoto['Q']
                self.QandAnswerLST[1] = valuesPhoto['A1']
                self.QandAnswerLST[2] = valuesPhoto['A2']
                self.QandAnswerLST[3] = valuesPhoto['A3']
                self.QandAnswerLST[4] = valuesPhoto['A4']
                print(self.QandAnswerLST)

        windowPhoto.close()

    def sendButtonFunction(self):

        return self.QandAnswerLST
        

