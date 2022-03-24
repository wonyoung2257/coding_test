import sys
sys.stdin = open('input_py.txt','r')

input = sys.stdin.readline

nums= list(input())
nums.sort(reverse=True)
print(''.join(nums))