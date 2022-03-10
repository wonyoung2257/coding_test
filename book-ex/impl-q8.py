s= 'AJKDLSI'

total = 0
for i in sorted(s):
  if ord(i)<65:
    total += int(i)
  else:
    print(i, end='')
print(total if total !=0 else '')