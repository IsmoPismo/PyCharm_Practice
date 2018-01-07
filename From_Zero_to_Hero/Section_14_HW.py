print("Problem 1")#Problem 1
def gensquares(N):
    for num in range(N):
        yield num**2

for x in gensquares(4):
    print(x, end=" ")


print("\n\nProblem 2")#Problem 2
import random

def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low, high)

for num in rand_num(1, 10, 4):
    print(num, end=" ")


print("\n\nProblem 3")#Problem 3
s = 'Larisa'
iter_s = iter(s)
for i in range(len(s)):
    print(iter_s.__next__(), end='-')


print("\n\nProblem 4")#Problem 4
print('If the output has the potential of taking up a '
      'large amount of memory and you only intend to iterate through it, '
      'you would want to use a generator.')


print("\nProblem 5 - Generator Comprehension")#Problem 5
list = ['g','e','n','e','r','a','t','e']
generate = (item for item in list)
print(next(generate))
print(generate.__next__())
print(next(generate))
print(generate.__next__())
print(next(generate))
print(generate.__next__())
print(next(generate))
print(generate.__next__())
