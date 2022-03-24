from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

import sys

sys.stdin = open('input_py.txt','r')

input = sys.stdin.readline

data = [1, 2, 3, 4]
result_p = list(permutations(data, 2))
result_c = list(combinations(data, 2))
result_pro = list(product(data, repeat=2))
result_cw = list(combinations_with_replacement(data, 2))

print(result_p)
print(result_c)
print(result_pro)
print(result_cw)