import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()


while M >0:
  n1, n2 = arr[0:2]
  arr.append(n1+n2)
  arr.append(n1+n2)
  arr.pop(0)
  arr.pop(0)
  arr.sort()
  M -=1
print(sum(arr))