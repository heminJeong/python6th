import sys
sys.setrecursionlimit(3000)

i = 0
def myfunc():
    global i
    i += 1
    print("My Function : ", i)
    myfunc()

myfunc()