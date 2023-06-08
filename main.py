def pw(x, y):
    z = x ** y
    print(z)

pw(2, 5)
pw(5, 2)

def show(name: str, age: int):
    print(f"Name: {name} Age: {age}")

show(name='정해민', age=30)

def add(x, y):
    z = x + y
    print("Addition : ", z)

add(5, 2)

def add(*num):
    z = num[0] + num[1] + num[2]
    print("Addition *: ", z)

add(5, 2, 4)

def add(x, *num):
    z = x + num[0] + num[1]
    print("Addition x *: ", z)

add(5, 2, 4)

def add(**num):
    z = num['a'] + num['b'] + num['c']
    print('Addition : ', z)

add(a = 5, b = 2, c = 4, d= 5)


a = 50

def show():
    x = 10
    print(x)
    print(a)

show()

print("Global Variable a : ", a)

def show2():
    global a
    print("show2-A :", a)
    a = 20
    print("show2-A2 :", a)

show2()
print("A : ", a)


i = 0
def myfun():
    print("My Function i : ", i)


    print("My function", a)

myfun()
print("Global Variable a : ", a)