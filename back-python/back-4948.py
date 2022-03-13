import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

n = 123456*2
a = [False, False] + [True]*(n-1)


for i in range(2, n+1):
  if a[i]:    
    for j in range(2*i, n+1, i):
      a[j] = False

while True:
  num = int(input())
  if num == 0:
    break
  cnt = 0
  for i in range(num+1, num*2+1):
    if a[i]:
      cnt+=1
  print(cnt)