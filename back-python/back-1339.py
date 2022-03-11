import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())

dic = {}
for i in range(N):
  word = list(input().strip())

  for j in range(0, len(word)):
    alphabet = word.pop()
    if alphabet in dic:
      dic[alphabet] += 10**j
    else:
      dic[alphabet] = 10**j

dic = sorted(dic.items(), key= lambda x:x[1], reverse=True)

print(dic)

total = 0
idx = 9
for k in dic:
  total += idx*k[1]
  idx-=1

print(total)