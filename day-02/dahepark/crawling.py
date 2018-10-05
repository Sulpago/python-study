import requests
from PIL import Image
from io import BytesIO

# 크롤링함수
def crawlingFunc(url):
    r = requests.get(url)
    # print(r.status_code)
    with open('test.txt', 'w') as f:
        f.write(str(r.status_code) + '\n' + url)
    print("saved")

# 크롤링 이미지 함수
def crawlingImgFunc(itemno):
    prefixurl = 'http://image.g9.co.kr/g/' + str(itemno) + '/n'
    r = requests.get(prefixurl)
    if r.status_code != 200:
        return

    with Image.open(BytesIO(r.content)) as im:
        im.save(str(itemno) + '.jpg')

# crawlingFunc('http://www.g9.co.kr')
def test():
    for no in range(1157541176, 1157541276):
        crawlingImgFunc(no)

class downloader():
    def c_test(self):
        test()

ttt= downloader()
ttt.c_test()
