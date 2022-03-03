import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

N, M  = map(int, input().split())

dic = {}
for i in range(N):
  web, pw = input().strip().split(' ')
  dic[web] = pw

for i in range(M):
  web = input().strip()
  print(dic[web])