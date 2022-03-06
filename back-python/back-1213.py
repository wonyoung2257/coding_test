import sys

sys.stdin = open("input_py.txt", "r")
input = sys.stdin.readline

s = list(input().strip())
arr= [0] * 26

for i in s:
  arr[ord(i)-65] +=1

odd = 0
odd_s = ''
even_s = ''

for i in range(26):
  if arr[i] % 2 == 1: # 알파벳이 홀수
    odd_s += chr(i + 65)
    odd += 1
    
  even_s += chr(i+ 65) * (arr[i] // 2)

if odd >1:
  print("I'm Sorry Hansoo")
else:
  print(even_s + odd_s + even_s[::-1])