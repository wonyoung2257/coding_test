import sys

sys.stdin = open("input_py.txt", "r")

T = int(input())
arr = [int(input()) for _ in range(T)]
result =[]
result.append(arr[0])
result.append(arr[0]+arr[1])
result.append(max(arr[0]+arr[2], arr[1]+arr[2]))

for i in range(3,T):  
  result.append(max(result[i-2]+arr[i], result[i-3]+arr[i]+arr[i-1])) 

print(result.pop())