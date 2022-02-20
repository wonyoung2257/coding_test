import sys

sys.stdin = open("../input_py.txt", "r")

testCase = int(sys.stdin.readline())

arr = []
for _ in range(testCase):
  num = int(sys.stdin.readline())
  
  if num != 0:
    arr.append(num)
  else:
    arr.pop()

print(sum(arr))