import sys
sys.stdin = open("input_py.txt", "r")

T = int(input())

for i in range(1, T+1):
  A, B = map(int, input().split(' '))
  sum = A+B
  if sum >= 24:
    print(f'#{i} {sum-24}')
  else:
    print(f'#{i} {sum}')