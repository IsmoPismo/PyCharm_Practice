#Decorators part1

s = "I'm global!"
def func():
    print (locals())

func()

print(globals()['s'])

def hello(name="Ismar"):
    return ("Hi " + name)


pozz = hello(name="Larisa")
del hello
print(pozz)


#Decorators part2


