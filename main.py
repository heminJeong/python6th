a = ['a1', 'a2', 'a3']

for i, v in enumerate(a):
    print([i, v])
print('-------------------')
i = 0
for v in a:
    print([i, v])
    i += 1
print('-------------------')
for i in range(len(a)):
    print([i, a[i]])