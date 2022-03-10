import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split(' '))

coin = [list(map(int, input().strip())) for _ in range(N)]

def xor(a,b):
  
  for i in range(a+1):
    for j in range(b+1):
      coin[i][j] ^= 1

cnt = 0
for i in range(N-1, -1, -1):
  for j in range(M-1, -1, -1):

    if coin[i][j] == 1:
      cnt +=1
      xor(i,j)
print(cnt)