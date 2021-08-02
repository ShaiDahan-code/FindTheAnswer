import requests as rq
from urllib.parse import urlencode,urlparse,parse_qs
from lxml.html import fromstring

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
#shai is a gay
class Search:

    def __init__(self, question, answer_1, answer_2, answer_3, answer_4):
        self.googleURL = "https://www.google.com/search?q=" + question
        self.poosible_answer = [[answer_1,0],[answer_2,0],[answer_3,0],[answer_4,0]]
        self.question = question
        self.listURLS = []
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
        #SAREL YOU ARE MORONG
        return listURLS

    def countTheAnswer(self):
        for site in self.listURLS:
            siteResponse = rq.get(site, headers=headers, allow_redirects=True)
            if siteResponse.status_code == 200:
                text = siteResponse.text.split()
                for word in text:
                    if(word in self.poosible_answer[0][0]):
                        self.poosible_answer[0][1] += 1
                    elif(word in self.poosible_answer[1][0]):
                        self.poosible_answer[1][1] += 1
                    elif (word in self.poosible_answer[2][0]):
                        self.poosible_answer[2][1] += 1
                    elif (word in self.poosible_answer[3][0]):
                        self.poosible_answer[3][1] += 1
            elif siteResponse.status_code == 404:
                print("Fail connect to Google site!")


    def searchAnswer(self):
        googleResponse = rq.get(self.googleURL, headers=headers, allow_redirects=True)
        if googleResponse.status_code == 200:
            self.listURLS = list(self.getHTTP(googleResponse.text))
            self.listURLS = self.listURLS[4:6]
        elif googleResponse.status_code == 404:
            print("Fail connect to Google site!")


    def getAnswer(self):
        biggest = self.poosible_answer[0][1]
        key = 0
        i = 0
        for countAnswer in self.poosible_answer:
            print(countAnswer[1])
            if countAnswer[1] > biggest:
                biggest = countAnswer[1]
                key = i
            i+=1
        print(self.poosible_answer[key][0])