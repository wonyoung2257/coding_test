N = input()

temp =''
count0 = 0
count1 = 0
for i in N:
  if temp == '':
    temp = i
    continue
  if temp == i: continue
  else:
    if temp == '0': count0 +=1
    else : count1 +=1
    temp = i

if temp == '0': count0 +=1
else : count1 +=1
print(min(count0, count1))