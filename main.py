def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


runner = fibonacci(100)

print(next(runner))
print("======")
print(runner)
print(next(runner))
print("=======")

for num in runner:
    print(num)


def generate_alphabet(start_letter, end_letter):
    start = ord(start_letter)
    end = ord(end_letter)
    while start <= end:
        yield chr(start)
        start += 1


runner = generate_alphabet('A', 'F')

for letter in runner:
    print(letter)
