#021
'''
e_o_o = int(input("Enter your number "))
def even_o_odd(num):
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Odd number")

even_o_odd(e_o_o)
'''

#022
'''
user_list = input("Enter your list with spaces between ")
real_list = list(map(int, user_list.split()))
print(real_list.count(4))
'''

#023
def kihanje(string, num):
    if len(string) > 2:
        print(string[:2]*num+string[2:])
    else:
        print('too short')

kihanje('Heyo',5)

#024
'''
def vowel(a):
    vows = ['a','e','o','i','u']
    for i in vows:
        if a != i:
            print("it's not a vowel")

vowel('b')
'''

#025
print(3 in [3, 4])

#026
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)

histogram([2, 3, 1, 7])

#027
def conc(list):
    result = ""
    for x in list:
        result += str(x)
    print(result)

conc([2,5,88])

#028
def print_no_237(list):
    for x in list:
        if x % 2 == 0:
            print(x)
        elif x == 237:
            break

#029
color1 = set(['black', 'white', 'blue'])
color2 = set(['blue'])

print(color1.difference(color2))    #.DIFFERENCE

#030
base = 2
height = 5
area = base*height/2
print(area)

#031
def gcd(x, y):
    gcd = 1

    if x % y == 0:
        return y

    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

print(gcd(120, 20))
print(gcd(45, 60))

#032
def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm
print(lcm(4, 6))
print(lcm(15, 17))

#033
def tri_vals(x, y, z):
    if x==y==z:
        return 0
    else:
        return x+y+z

print(tri_vals(2,2,2))
print(tri_vals(1,2,3))

#034
def sum_between(x, y, z):
    f = x + y + z
    if f in range(15,20):
        return 0
    else:
        return f

print(sum_between(5,5,8))

#035
def stupid_func(x, y):
    return x == y or abs(x+y) == 5 or abs(x-y) == 5

print(stupid_func(5,10))

#036
def adds_if_ints(x, y):
    if type(x) == int() and type(y) == int():
        return x + y

def add_if_ints2 (x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        return ("Not an Int")
    else:
        return x +y

print(adds_if_ints('a',5))
print(add_if_ints2("2",1))

#037
def display(name, age, adress):
    print("Name {}\nAge {}\nAdress {}".format(name, str(age), adress))

display('Ismar',29,'Sedata Karica')

#038
x = 4
y = 5
z = (x+y)**2
print(z)

#039
amount = 1000
int = 3.5
years = 7
int_in_percent = 3.5/100
future = (amount * int_in_percent) * years
