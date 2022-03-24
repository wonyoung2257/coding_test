import sys
sys.stdin = open('input_py.txt','r')

input = sys.stdin.readline

n = int(input())
nums = list(map(int ,input().split()))
temp = list(set(nums))
temp.sort()

dict = {}
cnt = 0
for i in temp:
  dict[i] = cnt
  cnt+=1

for num in nums:
  print(dict[num], end =' ')