import sys
sys.stdin = open("input_py.txt", "r")

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

print(board)