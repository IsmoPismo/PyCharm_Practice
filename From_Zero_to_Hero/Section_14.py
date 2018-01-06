#Generator
def cube_nums(n):
    for i in range(n):
        yield i**3

print(list(cube_nums(15)))


#Generator II
def finaboči(n):
    '''
    Generate a finaboči moči
    :param a:   first num
    :param b:   second num
    :return:    finabučii!!~!!
    '''
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

print(list(finaboči(5)))


#next() and iter()
def simp_gen():
    for i in range(3):
        yield ('next() ! ' + str(i))

gen_var = simp_gen()
print(next(gen_var))
print(next(gen_var))
print(next(gen_var))
#print(next(gen_var)) #StopIteration


s = 'hello'
#Iterate over string
for let in s:
    print (let)

print("TypeError: str object is not an iterator!!!!!!")

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


