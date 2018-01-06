
#Open with w(PLUS), write and close
aria = open("Aria.txt","w+")

for i in range(10):
    aria.write("This is Us {}\n".format(i+1))

aria.close()

#Append - Plus indicates if no file ==> Create file
aria = open("Aria.txt","a+")

for i in range(3):
    aria.write("The Simpsons\n")



#Read files
aria = open("Aria.txt","r")
if aria.mode == "r":
    content = aria.read()
    print(content)
