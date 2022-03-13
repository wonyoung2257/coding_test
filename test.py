# N = 2
# arr= [('홍길동', 95), ('이순신', 77)]

# arr = sorted(arr, key= lambda arr:arr[1])

# print(arr)

arr =[i for i in range(10)]

def fun(x):
  return x*2

arr2 = list(map(fun, arr))
print(arr2)