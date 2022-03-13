import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
ans = N
for _ in range(N):
  s = input().strip()
  temp = ''
  answer = []
  for i in s:
    if temp == '':
      temp = i
    if temp != i:
      if i in answer:
        ans-=1
        break
      else:
        answer.append(temp)
        temp = i
print(ans)