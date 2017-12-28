#Raw String

print ('C:\some\none <== "Wrong')
print (r'C:\some\none <== "Right"')


#Multy-Line String

print ('''
String literals can span multiple lines. 
One way is using triple-quotes: """...""" or \'\'\'...\'\'\'. 
End of lines are automatically included in the string, 
but it’s possible to prevent this by adding a \ \
at the end of the line. The following example:
''')

print ('''\
    Another Example     is to write \\ in the 1st line
    So it's             compleatly ignored
''')


#Concatenate

print ('Two or more string literals' 'next to each other are automatically''...')


#Out of Range Slicing

word = 'Python'
print ('''\
    word[42]  ERROR: the word only has 6 characters 
    However out of range slice indexes are handled gracefully when used for slicing:
    word[4:42] ==> 'on'
    word[42:] ==> ''
    ''')

