from re import M

arr = [0, 4,5,7,2,3,1,9,8]

# 선택 정렬
for i in range(len(arr)):
  min_index = i
  for j in range(i+1, len(arr)):
    if arr[min_index] > arr[j]:
      min_index = j
  arr[i], arr[min_index] = arr[min_index] , arr[i]

print(arr)

arr = [0, 4,5,7,2,3,1,9,8]

# 삽입 정렬
for i in range(1,len(arr)):
  for j in range(i, 0, -1):
    if arr[j] < arr[j-1]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
    else:
      break

print(arr)

arr = [5, 7, 9,0,3,1,6,2,4,8]

def quich_sort(arr, start, end):
  if start >=end:
    return
  pivot = start
  left = start+1
  right = end
  while left <= right:
    while left <= end and arr[left] <= arr[pivot]:
      left+=1
    while right > start and arr[right] >= arr[pivot]:
      right -=1
    if left > right:
      arr[right], arr[pivot] = arr[pivot], arr[right]
    else:
      arr[left], arr[right] = arr[right], arr[left]
  quich_sort(arr, start, right-1)
  quich_sort(arr, right+1, end)

quich_sort(arr, 0, len(arr)-1)
print(arr)
