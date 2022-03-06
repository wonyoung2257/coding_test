N, M = 5, 3
data = [1,3,2,3,2]

arr = [0]*11
for i in data:
  arr[i]+=1

total = 0
for i in range(1, M):
  temp = 0
  if arr[i] == 0:
    continue
  for j in range(i+1, len(arr)):
    temp += arr[i]*arr[j]
  total += temp

print(total)