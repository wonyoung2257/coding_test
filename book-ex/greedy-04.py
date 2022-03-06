n = [1,2,3,8]
n.sort()

target = 1
for x in n:
  if target<x:
    break
  target+=x

print(target)