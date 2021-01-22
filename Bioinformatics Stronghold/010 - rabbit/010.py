months = 35
pairs = 4

parent = 1
child = 1

for i in range(months-1):
    child, parent = parent, parent + (child * pairs)

print(child)