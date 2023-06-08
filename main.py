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