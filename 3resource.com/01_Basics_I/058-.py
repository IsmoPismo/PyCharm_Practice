#058
'''
from functools import reduce
n = int(input("Enter your number: "))
print(reduce(lambda x, y: x + y, range(n)))
'''

#059
'''
n = input('Enter height, please ')
feet = int(n[0])
inches = int(n[2:])

centimeter = feet * 30.48 + inches * 2.54
print('{a} is {b}cm'.format(a=n, b=centimeter))
'''

#060
import math
a = 2
b = 3
c = math.sqrt(a**2 + b**2)
print(c)

#061
feet = 1
print("{} feet is {} inces".format(feet, feet*12))
print("{} feet is {} yards".format(feet, feet*0.333333))
print("{} feet is {} miles".format(feet, feet*0.00018939375))

#062
minutes = 5
hours = 2
day = 3
weeks = 6
print("{} minutes is {} seconds".format(minutes, minutes*60))
print("{} hours is {} seconds".format(hours, hours*60*60))
print("{} days is {} seconds".format(day, day*60*60*24))
print("{} minutes is {} seconds".format(weeks, weeks*60*60*24*7))

#063
def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')
print("Absolute file path: ",absolute_file_path("test.txt"))

#064
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("test.txt")))

