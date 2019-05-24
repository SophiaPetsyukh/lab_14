from random import choice

def open(filename):
    with open(filename, encoding='utf-8') as f:
        data = []
        for el in f.readlines():
            data.append(el.strip())
    return data

def get_random_1000():
    result = []
    data = open('words.txt')
    for i in range(10000):
        word = choice(data)
        result.append(word)
        data.remove(word)
    return result

def search_lst():
    pass
