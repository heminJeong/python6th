stu = {101: 'Kim', 102: 'Bae', 103: "Hong"}
fees = {'Kim': 2000, 'Bae': 3000, 'Hong': 8000}
print(stu[101])
print(stu[102])
print(stu[103])

print(fees['Kim'])
print(fees['Bae'])
print(fees['Hong'])

stu[101] = 'Python'
print(stu)

stu[104] = '멋쟁이사자'

print(stu)

del stu[102]

print(stu)

new_stu = stu.copy()

key = (101, 102, 103)
value = '멋쟁이사자'


new_stu = dict.fromkeys(key, value)
print(new_stu)

print(stu[101])
print(stu.get(101))
print(stu.items())
print(stu.keys())
print(stu.values())