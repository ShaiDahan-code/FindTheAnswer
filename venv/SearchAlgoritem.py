import requests as rq
from urllib.parse import urlencode,urlparse,parse_qs
from lxml.html import fromstring


class Search:
    question = ""
    poosible_answer_1 = ""
    poosible_answer_2 = ""
    poosible_answer_3 = ""
    poosible_answer_4 = ""
    ansewr = ""
    googleURL = ""

    def __init__(self,question, answer_1,answer_2,answer_3,answer_4,):
        self.googleURL = "https://www.google.com/search?q=" + question
        self.poosible_answer_1 = answer_1
        self.poosible_answer_2 = answer_2
        self.poosible_answer_3 = answer_3
        self.poosible_answer_4 = answer_4
        self.question = question
        print("Init suuces!")


    def getHTTP(self , text):
        print()
        listURLS = []
        new_word = ""
        for word in text.split('href="'):
            if(word.startswith("http")):
                for i in word:
                    if i != '"':
                        new_word += i
                    else:
                        break
                listURLS.append(new_word)
                new_word = ""
        for i in listURLS:
            print(i)


    def searchAnswer(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        googleResponse = rq.get(self.googleURL, headers=headers, allow_redirects=True)
        if googleResponse.status_code == 200:

            print(googleResponse.text)
            self.getHTTP(googleResponse.text)

            print("Enter to Google site!")
        elif googleResponse.status_code == 404:
            print("Fail connect to Google site!")








    def getAnswer(self):
        return answer
