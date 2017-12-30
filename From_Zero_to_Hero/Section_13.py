print('Decorators part1')#Decorators part1

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


print('\nDecorators part2')#Decorators part2

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
print('Bez zagrade je SAMA funkcija, nije EXEcuted')
print(y)


print('\nDecorators part3')#Decorators part3

def hello(name='Jose'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Jose':
        return greet
    else:
        return welcome

x=hello()
print(x)


print('\nDecorators part4')#Decorators part4

def fukcija():
    return ('Jebeš mu mater')

def funkcija2():
    return ('Jebi mu mamu!')

def druga_funkcija(fank):
    print('Ova funkcija printa drugu funkciju: ')
    return(fank())

print (druga_funkcija(fukcija))
print (druga_funkcija(fukcija))


print('\nCreating a Decorator') #Creating a Decorator

def dekorator(fukcionalnost):
    def wrap():
        print ('Ovo se prvo vidi')
        fukcionalnost()
        print('Ovo je poslije')

    return wrap()

def fukcija_za_decorisat():
    print ('Meni treba decorator')

@dekorator
def fukcija_za_decorisat():
    print ('Meni treba decorator')

print (fukcija_za_decorisat)
