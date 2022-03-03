import sys

sys.stdin = open("./input_py.txt", "r")
input = sys.stdin.readline

N  = int(input())
arr = sorted(list(map(int, input().split(' '))))

result=[0]
for idx, val in enumerate(arr):
  result.append(val+result[idx])
print(sum(result))