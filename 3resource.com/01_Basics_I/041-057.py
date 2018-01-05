#041
import os.path

print(os.path.isfile("file.txt"))

#042
import platform
print(platform.architecture())

#043
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())

#044
import site;
print(site.getsitepackages())

#045
from subprocess import call
call(["ls", "-l"])

#046
print("Current File Name : ",os.path.realpath(__file__))

#047
import multiprocessing
print(multiprocessing.cpu_count())

#048
string = "245.88"
print(float(string))
print(int(float(string)))

#049

#050
for i in range(0, 10):
    print('*', end="")

#051
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

#052
def eprint(*args, **kwargs):
    print(*args, **kwargs)

eprint("abc", "efg", "xyz", sep="--")

#053

#054
import getpass
print(getpass.getuser())

#055
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

#056

#057
import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))
