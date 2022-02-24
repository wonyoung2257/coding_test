# 풀이 방법
# 3가지 연산 중 가능한 연산을 실행 했을 때 나오는 횟수 +1 이 가장 작은 수를 찾는다.
import sys

sys.stdin = open("./input_py.txt", "r")

T = int(sys.stdin.readline())

arr = [0]*1000001
arr[1] = 0
arr[2] = 1

for i in range(2, T+1):
  if T == 1:
    print(0)
    break
  
  arr[i] = arr[i-1]+1
  if i % 3 == 0:
    arr[i] = min(arr[i], arr[i//3]+1)
  if i %2 == 0:
    temp = arr[int(i/2)] +1
    arr[i] = min(arr[i], arr[i//2] +1)  

print(arr[T])

for i in range(2, T+1):

  num = 99999999999
  temp = 0
  if i %3 == 0:
    temp = arr[i//3] +1
    num = min(num, temp) 
  if i %2 == 0:
    temp = arr[i//2] +1
    num = min(num, temp)
  temp = arr[i-1] +1
  num = min(num, temp)
  arr[i] = num