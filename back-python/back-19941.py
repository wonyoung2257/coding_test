import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split(' '))
table = list(input().strip())

cnt = 0
for idx, val in enumerate(table):
  if val =='P':
    for i in range(max(idx-K, 0), min(idx+K+1, N)):
      if table[i] =='H':
        cnt+=1
        table[i] = 'O'
        break

print(cnt)
