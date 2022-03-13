# s = input().strip()
s = 'UNUCIC'
arr = [0,0 ,0,'ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

total = 0
for i in s:
  for j in range(3, len(arr)):
    if i in arr[j]:
      total+=j
      break

print(total)
