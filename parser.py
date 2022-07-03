import requests
import re
from random import randint
from fake_headers import Headers


async def photo_parser(message):
    headers = Headers(headers=True).generate()
    req = requests.get("https://yandex.ru/images/search?text=" + message, headers=headers)
    print(req.text)
    ph_links = list(
        filter(lambda x: x.startswith('http') and x.endswith('.jpg'), re.findall('''(?<=["'])[^"']+''', req.text)))
    print(ph_links)
    ph_list = []

    for i in range(len(ph_links)):
        ph_list.append(ph_links[i])

    del ph_links
    im = requests.get(ph_list[randint(0, len(ph_list))])
    out = open("temp/img.jpg", "wb")
    out.write(im.content)
    out.close()
