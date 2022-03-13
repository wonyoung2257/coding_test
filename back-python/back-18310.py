import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()

print(arr[(N-1)//2])