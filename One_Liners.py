def word_lengths(phrase):
    return map(lambda x: len(x),phrase.split())

print(list(word_lengths('How long are the words in this phrase!! Halleluyaa')))

from functools import reduce


def digits_to_num(digits):
    return reduce(lambda x, y,: (x *10 + y), digits)

print (digits_to_num([3,4,3,2,1]))

def filter_words(w, l):
    return filter(lambda x: x[0] == l, w)

lista = ['hey','geyx','sexy','hamburger']
print (list((filter_words(lista, 'h'))))

