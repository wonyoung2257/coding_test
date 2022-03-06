import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
arr= []

for i in range(N):
  s, e = map(int, input().split(' '))
  arr.append((s,e))
arr = sorted(arr, key = lambda x:x[0] )
arr = sorted(arr, key = lambda x:x[1] )
last = 0
cnt = 0

for i , j in arr:
  if i >=last:
    cnt+=1
    last = j

print(cnt)