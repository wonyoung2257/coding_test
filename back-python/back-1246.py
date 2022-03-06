import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N ,M = map(int, input().split(' '))
arr = [int(input()) for _ in range(M)]

arr.sort(reverse=True)
result = []
for i, v in enumerate(arr) :
  if i+1 > N:
    break

  result.append(((i+1) * v, v))

result.sort(reverse= True)
print(result[0][1],result[0][0])