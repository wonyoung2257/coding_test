import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

string = input().split('-')
arr = []
for i in string:
    cnt  =sum(list(map(int, i.split('+'))))
    arr.append(int(cnt))

n = arr[0]

for i in range(1, len(arr)):
    n -= arr[i]
print(n)