a = {10, 20, 30, '정해민', 'Jeong', 40, 10, 20}

b = set()
print(type(a))
print(type(b))

print(a)

a.remove('정해민')
a.discard('멋쟁이사자')
a.discard(70)

new_set = {10, 20, 50, 70, 80}

intersection_a_new = a.intersection(new_set, a, b)
print(intersection_a_new)

union_a = a.union(new_set)
print('union_a : ', union_a)

difference_a = a.difference(new_set)
print("difference_a : ", difference_a)

print(b.issubset(a))
print(a.issuperset(b))

sym_a = a.symmetric_difference(new_set)
print('symmetric_difference : ', sym_a)