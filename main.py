def val(lst):
    print("Inside Function Before Append : ", lst, id(lst))
    lst.append(4)
    print("Inside Function After Append : ", lst, id(lst))

lst = [1, 2, 3]
print("Before Calling Function : ", lst, id(lst))
val(lst)
print("After Calling Function : ", lst, id(lst))