import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline.strip

s = input().split(input())
print(len(s)-1)
