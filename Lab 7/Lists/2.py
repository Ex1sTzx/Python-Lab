from operator import mul
from functools import reduce
arr = [1,2,3,7,8,9,10,11,12,13,14,15]
print(reduce(mul,arr))