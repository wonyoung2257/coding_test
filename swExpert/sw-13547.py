import sys
sys.stdin = open("input_py.txt", "r")
T = int(input())

for _ in range(T):
  s = input()
  last = 15-len(s)
  cnt = 0
  for i in s:
    if i == 'o':
      cnt+=1
  if cnt + last >=8:
    print(f'#{_+1} YES')
  else:
    print(f'#{_+1} NO')