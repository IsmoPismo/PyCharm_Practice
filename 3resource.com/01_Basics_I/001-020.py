#001
print('''\n
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
	''')


#002
import sys
print(sys.version_info)


#003
import datetime
now = datetime.datetime.now()
print(now.strftime("\n%Y-%m-%d %H:%M:%S"))


#004
'''
radius = int(input("\nEnter radius: "))
Area = radius * 3.14
print("The Area of this circle is " + str(Area))
'''

#005
'''
name = input("\nEnter your name: ")
sur = input("Enter your last name: ")
print(sur, name)
)'''

#006
'''
values = input("\nInput some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
'''

#007
'''
filename = input("Enter the full file name ")
print(filename.split('.')[-1])
'''

#008
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0] + ' ' + color_list[-1])


#009
exam_st = (11, 12, 2014)
print( "The examination will start from : %i / %i / %i"%exam_st)


#010
'''
n = int(input("\nEnter your input: "))
n1 = int( "%s" % n)
n2 = int( "%s%s" % (n, n))
n3 = int( "%s%s%s" % (n, n, n))
print(n1 + n2 + n3)
'''

#011
print(abs.__doc__)


#012
'''
import calendar
m = int(input("Enter month "))
y = int(input("Enter year "))
print(calendar.month(y, m))
'''

#013
print('''
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
''')

#014
'''
from datetime import date
date1 = input("Enter date in format YYYY-MM-DD ")
year, month, day = map(int, date1.split('-'))
date2 = input("Enter second date in same format (YYYY-MM-DD) ")
year2, month2, day2 = map(int, date2.split('-'))
d0 = date(year, month, day)
d1 = date(year2, month2, day2)
delta = d1 - d0
print(delta.days)
'''

#015
radius = 6
volume = 3/4*3.14*radius**3
print("Volume is {a}".format(a=volume))
