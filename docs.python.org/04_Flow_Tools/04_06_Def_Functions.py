#Tricks

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""     #It's good practice to write DocStrings
    a, b = 0, 1
    while a < n:
        print (a, end=' ') #StackOverflow
        a, b = b, a+b

fib(88)


#Default Argument Values

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'): #Only NEEDS the prompt argument
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

#This example also introduces the in keyword.
#This tests whether or not a sequence contains a certain value.


