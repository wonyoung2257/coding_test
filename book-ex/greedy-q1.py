N = 5
arr = [2, 3,4,3,5]
arr.sort()

cnt = 0
while len(arr) > 0:
  temp = arr[0]
  if temp ==1:
    cnt+=1
    arr.pop(0)
  else:
    i = 0
    while temp >i:
      try:
        temp = arr.pop(0)
        i+=1
      except:
        cnt-=1
        break
    cnt+=1


print(cnt)