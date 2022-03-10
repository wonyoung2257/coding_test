import sys
sys.stdin = open("input_py.txt", "r")

T  = int(input())
answer = []
for i in range(1, T+1):
  a, b, c, d = map(int, input().split())
  arrA = [0] * 101
  arrB = [0] * 101
  
  for j in range(a,b):
    arrA[j] = 1
  for j in range(c, d):
    arrB[j] = 1
  cnt = 0
  for k in range(max(a,b,c,d)+1):
    if arrA[k] ==1 and arrB[k] ==1:
      cnt+=1
  
  answer.append(cnt)

for idx, val in enumerate(answer):
  print(f'#{idx+1} {val}')