def word_lengths(phrase):
    return map(lambda x: len(x),phrase.split())

print(list(word_lengths('How long are the words in this phrase!! Halleluyaa')))

from functools import reduce


def digits_to_num(digits):
    return reduce(lambda x, y,: x *len(digits), reversed(digits))

print (digits_to_num([3,4,3,2,1]))
