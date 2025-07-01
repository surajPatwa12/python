a={54,6,34,53}
b={3,45,6,45}

print(type(a))

a.add(65)
print(a)

print(a.difference(b))

print(a.union(b))

print(a.intersection(b))

print({3,45}.issubset(b))

print(a.pop())

a.clear()
print(a)