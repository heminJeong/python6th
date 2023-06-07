print("인자가 없는 함수")

def disp():
    name = "멋쟁이사자"
    print("Welcome to", name)


print("함수 실행")
disp()
disp()
disp()

def add(y):
    x = 10.2334
    print(x + y)
    print(f"Formatted Output {x + y:5.2f}")

add(20)