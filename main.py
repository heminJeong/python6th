b = (10)
c = (10, )

print(type(b))
print(type(c))

d = (10, 20, 30, 40)
e = (10, 20, -50, 21.3, '멋쟁이사자')
f = 10, 20, -60, 21.3, '멋쟁이사자'

print(d, e, f, sep='\n')

print(f[1])
print(f[2])
print(f[3])
print(f[4])

print(f[:3])
print(f[1:4])
print(f[3:])


h = (10, 20, -50, 20)
print(min(h), max(h))
print(h.count(20))
print(h.index(20))

a = (10, 20, -50)
x, y, z = a
print(x, y, z)

a = 1
b = 2

print("a : ", a)
print("b : ", b)

a, b = b, a

print("a : ", a)
print("b : ", b)