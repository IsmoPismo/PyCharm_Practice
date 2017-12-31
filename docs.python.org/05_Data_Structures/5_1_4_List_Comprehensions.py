#List of Squares

squares = [x**2 for x in range(10)]
print(squares)


#Tuples

print ([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
print()

#Examples

vec = [-4, -2, 0, 2, 4]
print([x*2-10 for x in vec])            # create a new list
print([x-100 for x in vec if x < 0])    # filter the list
print([abs(x) for x in vec])            # apply a function

fresh_fruit = [' banana ', ' blueberry ', ' bostan ']
print([str.strip() for str in fresh_fruit])                 # call a method

print([(x, x**2) for x in range(6)])                        # create a list of 2-tuples

