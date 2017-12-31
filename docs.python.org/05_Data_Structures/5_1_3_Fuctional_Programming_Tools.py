#Filter
print('Filer() built-in Function:')

def f(x): return x % 3 == 0 or x % 5 == 0
filter_list = filter(f, range(1,28))
print (list(filter_list))


#Map
print('\nMap() built-in Fuction:')

def cube(x): return x**3
map_list = map(cube, range(1,13))
print(list(map_list))

print('\nThe function must then have as many arguments as there are sequences')
print(list(map(lambda x, y: x+y, range(5), range(5))))


#Reduce
print('\nReduce() built-in Function')
from functools import reduce
print(reduce(lambda x, y: x*10+y, range(10)))
