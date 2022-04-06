import random
temp = []
n = 1024
while len(temp) != n**2:
  ran = random.randrange(0,n**2)
  if ran not in temp:
    temp.append(ran)
  
print(n)
for i in range(n):
  print(*temp[n*i:n*i+n])