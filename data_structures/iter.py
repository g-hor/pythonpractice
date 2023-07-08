names = ['sara', 'kaiter', 'milner']

name_iter = iter(names)

print(name_iter)

first = next(name_iter)
second = next(name_iter)
third = next(name_iter)

print(first)
print(second)
print(third)

print(name_iter)

print('sara' in names)

for name, idx in enumerate(names):
  print(name)
  print(idx)

for i in range(10, 0, -1):
  print(i)


