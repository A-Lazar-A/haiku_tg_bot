from random import sample


async def rnd_haiku():
    file = open('haiku.txt')
    return sample(file.readlines(), 3)
