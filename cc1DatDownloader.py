import requests
from pathlib import Path
from html.parser import HTMLParser
import time

def download_and_save_set(set_name):
    levelset = requests.get('https://bitbusters.club/gliderbot/sets/cc1/' + set_name)
    file = open("levelsets/" + set_name, "wb")
    file.write(levelset.content)
    file.close()

class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.last_tag_was_a_dat = False
        self.dat_name = None
        HTMLParser.__init__(self)

    def handle_data(self, data):
        if data.find(".dat") != -1:
            self.last_tag_was_a_dat = True
            self.dat_name = data[0:data.find(".dat")+4]
        elif self.last_tag_was_a_dat == True:
            self.last_tag_was_a_dat = False
            online_size = int(str(data).split()[2])
            try:
                download_size = Path('levelsets/' + self.dat_name).stat().st_size
            except Exception:
                download_size = 0
            if online_size != download_size:
                download_and_save_set(self.dat_name)
                print("Successfully downloaded " + self.dat_name)
            else:
                print(self.dat_name + " is already downloaded.")

r = requests.get('https://bitbusters.club/gliderbot/sets/cc1/')

parser = MyHTMLParser()
parser.feed(r.text)