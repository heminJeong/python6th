fruits = ['apple', 'banana', 'cherry', 'orange']
vegetables = ['carrot', 'cucumber']

grocery = fruits + vegetables
print(grocery)

numbers = [10, 5, 8, 1, 7]
numbers.sort()

print(numbers)

slice_numbers = numbers[1:4]

print(slice_numbers)

numbers_copy = numbers.copy()
print(numbers_copy)

numbers_clone = numbers[:]
print(numbers_clone)



alias_number = numbers
print(alias_number)

alias_number.pop()

# 사용자 입력으로 리스트 만들기

user_input_list = []
num_elements = int(input("Enter Number of Element : "))
for i in range(num_elements):
    user_input_list.append(input("Enter Element : "))

print("User Input List : ")
for elemnet in user_input_list:
    print(elemnet)