# binery_search 정리
"""
target을 찾을 때
target에 조건에 맞을 때 출력함

target이 없으면 어떻게 하나??

탈출조건: start < end 일 때
start = mid +1
end = mid

탈출 조건: start <= end 일 때
start = mid +1
end = mid -1

왜?

"""
import bisect
arr = [1, 2, 2, 3, 3, 3, 4, 6] 

target = 4

start = 0
end = len(arr)-1
# val 값이 있을 때 처음 나오는 값
# val 값이 없을 때 들어가야할 곳
print(bisect.bisect_left(arr, 3)) # -> lowerBound
# val 값이 있을 때 해당 값이 가장 마지막에 있는 위치
# val 값이 없을 때 들어가야할 곳
print(bisect.bisect_right(arr, 3)) # -> upperBound
# while start < end:
#   mid = (start + end) //2

#   if target == arr[mid]:
#     print('찾음', mid)
#     break
#   elif target > arr[mid]:
#     start = mid +1
#   else:
#     end = mid

# print(mid)

"""
lower/upper bound
- 원하는 값보다 처음으로 크거나 작은 값이 나오는 위치 찾는 방법
- 중복된 요소나 타겟의 상한 하한을 찾는 경우 등 사용
lower: 타켓보다 같거나 큰 값이 나오는 처음 위치
upper: 타켓보다 처음으로 큰 값이 나오는 위치
"""
arr = [1, 2, 2, 3, 3, 3, 4, 6]

start = 0
end = len(arr)-1
target = 2
while start < end:
  mid = (start+end) //2
  if target < arr[mid]:
    end = mid
  else:
    start= mid+1
print(start)
