from math import factorial
import sys
sys.stdin = open("input_py.txt", "r")
N, M = map(int, input().split())
print((factorial(N)//(factorial(N-M)*factorial(M))))