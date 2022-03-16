from bisect import bisect_left, bisect_right
import sys
sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline


N, x = map(int,input().strip().split(' '))
x = 2
arr = list(map(int, input().split(' ')))
print(arr)
print(bisect_left(arr, x))
print(bisect_right(arr,x))