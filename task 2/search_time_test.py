from random import choice
from task1.linkedbst import LinkedBST
from time import time

def read(filename):
    with open(filename, encoding='utf-8') as f:
        data = []
        for el in f.readlines():
            data.append(el.strip())
    return data

def get_random_10000():
    result = []
    data = read('words.txt')
    for i in range(10000):
        word = choice(data)
        result.append(word)
        data.remove(word)
    return result

def search_lst(dictionary, words):
    result = []
    for word in dictionary:
        if word in words:
            result.append(word)
    return result

def build_tree(data):
    tree = LinkedBST()
    for word in data:
        tree.add(word)
    return tree

def search_tree(tree, words):
    result = []
    for el in words:
        if tree.__contains__(el):
            result.append(el)
    return result

if __name__ == '__main__':
    words = get_random_10000()
    dictionary = read('words.txt')
    tree = build_tree(dictionary)

    start1 = time()
    search_tree(tree, words)
    print(time() - start1)
    start2 = time()
    search_lst(dictionary, words)
    print(time() - start2)
    
