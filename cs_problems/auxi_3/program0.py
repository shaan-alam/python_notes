# FEB 3
# Example of deep and shallow copy 

import copy
a = [1,2,3,[4,5]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[3][0] = 10

print (a)
print (b)

print (c)