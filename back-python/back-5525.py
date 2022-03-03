import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
PN = 'IOI'
for i in range(1,N):
  PN+='OI'

cnt = 0
for i in range(M-len(PN)+1):
  if S[i] =='O':
    continue
  if S[i:i+len(PN)] == PN:
    cnt+=1

print(cnt)