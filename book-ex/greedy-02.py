import time
n, k = 10000000000, 17

result = 0
start_t = time.time()
print(start_t)
while n >= k:
  while n%k !=0:
    n-=1
    result +=1
  n //=k
  result +=1

while n > 1:
  n -= 1
  result +=1


end_t = time.time()
print(end_t)
print(end_t - start_t)
print(result)

# target = (n//k) *k
#   result += (n-target)
#   n = target
#   if n<k:
#     break
#   result +=1
#   n//=k