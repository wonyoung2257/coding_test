arr = [True] * 10001

for i in range(1, len(arr)):
  temp = list(str(i))
  for j in temp:
    i+= int(j)
  if i < 10001:
    arr[i] =False  
  

for i in range(1, len(arr)):
  if arr[i]:
    print(i)

