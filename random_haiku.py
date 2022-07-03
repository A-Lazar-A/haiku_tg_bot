from random import sample


async def rnd_haiku():
    file = open('haiku.txt')
    text = file.readlines()
    file.close()
    return sample(text, 3)
