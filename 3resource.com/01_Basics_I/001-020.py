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
