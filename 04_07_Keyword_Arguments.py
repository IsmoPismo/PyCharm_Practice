def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print (action + voltage + type + state)

#This funkction call be called:

parrot('10')                                          # 1 positional argument
parrot(voltage="10")                                  # 1 keyword argument
parrot(voltage="10000", action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage="10000")             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
print ('\n')


#*args and *kwargs

def cheeseshop(**kwargs):
    for kw in kwargs:
        print (kw, ":", kwargs[kw])

cheeseshop(shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#Another example

def input_username(**kwargs):
    lista = {}
    for kw in kwargs:
        lista[kw] = kwargs[kw]

    return lista


first_user = input_username(username="Ismar", nickname="Ismo", surname="Sacirovic")
second_user = input_username(username="Larisa",nickname="Laca",surname="Brkic")

print (first_user)
print (second_user)

Ismar_user = first_user.values('username')

