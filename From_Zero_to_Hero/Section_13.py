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

def hoi(name='Ismar'):
    print ("Hoi() Executed")
    def cao():
        return ('''\
        Ovo je cao\
            ''')
    def welcome():
        return ('''\
        Wellcome xD\
        ''')

    print(cao())
    print(welcome())
    print ('Sad smo vanka u hio()')


hoi()
y = hoi
y()
print(y)
