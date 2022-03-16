import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input().strip())

# arr = list(map(int, input().strip().split(' ')))

# arr.sort()

# def binery_search(start, end, target):
#   while start <= end:
#     mid = (start + end) //2

#     if target == arr[mid]:
#       return True
#     elif arr[mid] > target:
#       end = mid -1
#     else:
#       start = mid +1
  
#   return False

# if binery_search(0, len(arr)-1, N):
#   print('YES')
# else:
#   print('NO')
