import requests
import re
from random import randint
from fake_useragent import UserAgent


async def photo_parser(message):
    ua = UserAgent()
    req = requests.get("https://yandex.ru/images/search?text=" + message, headers={'User-Agent': ua.random})
    print(req)
    ph_links = list(filter(lambda x: '.jpg' in x, re.findall('''(?<=["'])[^"']+''', req.text)))
    print(ph_links)
    ph_list = []

    for i in range(len(ph_links)):
        if ph_links[i][0:4] == "http":
            ph_list.append(ph_links[i])

    del ph_links
    im = requests.get(ph_list[randint(0, len(ph_list))])
    out = open("temp/img.jpg", "wb")
    out.write(im.content)
    out.close()
