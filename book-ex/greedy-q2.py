N = '567'

total = 1
for i in N:
  if i == '0':
    continue
  total *= int(i)

print(total)