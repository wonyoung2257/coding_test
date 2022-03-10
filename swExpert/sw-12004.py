import sys
sys.stdin = open("input_py.txt", "r")


T  = int(input())
arr = []
for i in range(10):
  for j in range(10):
    arr.append(i*j)

for i in range(1, T+1):
  num = int(input())
  if num in arr:
    print(f'#{i} Yes')
  else:
    print(f'#{i} No')