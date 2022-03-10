import sys
sys.stdin = open("input_py.txt", "r")

T = int(input())

# for i in range(1,T+1):
#   num = input()
#   numArr = list(map(int, num))
  
#   maxNum = num
#   minNum = num
#   for idx, val in enumerate(numArr):
#     if val != max(numArr):
#       numArr


arr = [1,2,3,3,2,2]
print(arr.index(3))