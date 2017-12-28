#P1
def word_lengths(phrase):
    return map(lambda x: len(x),phrase.split())

print(list(word_lengths('How long are the words in this phrase!! Halleluyaa')))

'''
Lambda function was not needed because we have a built-in function to check the Length.
Fuction name is len(), and we do not write the () in map: >map(len, phrase.slit()<
'''

#P2
from functools import reduce
def digits_to_num(digits):
    return reduce(lambda x, y,: x *10 + y, digits)

print (digits_to_num([3,4,3,2,1]))

#P3
def filter_words(w, l):
    return filter(lambda x: x[0] == l, w)

lista = ['hey','geyx','sexy','hamburger']
print (list((filter_words(lista, 'h'))))

#P4
def concatenate(L1, L2, connector):
    return [word1+connector+word2 for (word1, word2) in zip(L1,L2)]

print (concatenate(['A','B'],['a','b'],'-'))

#P5
def d_list(L):
    return {key:num for num,key in enumerate(L)}

print (d_list(['a','b','c']))

#P6
def count_match_index(L):
    return len([num for count,num in enumerate(L) if num == count])

print (count_match_index([0,1,2,5,6,6,6,11,11,11]))
