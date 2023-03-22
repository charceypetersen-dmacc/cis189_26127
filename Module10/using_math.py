# Following lines demonstrate importing definitions from module
from my_math import PI, operations, mean

print(mean([1, 2, 3, 4, 5]))

print(PI)
print(operations)

for item in operations:
    print(item)

# Following lines demonstrate different ways of importing definitions - comment in and out each set to understand behabior

# # importing specific definitions, can access by name
# from my_math import mean, operations, PI
# print(operations)
#
# # importing everything with star, can access any definition by name
# from my_math import *
# print(operations)
#
# # importing the module (but nothing specific, yet), access with {module name}.{definition name}
# import my_math
# print(my_math.operations)

# Following lines demonstrate how to avoid name collisions with imports
from my_math import mean
from statistics import mean
# ^ with the above lines, mean from statistics is what would execute

from my_math import mean as my_mean
from statistics import mean
# ^ now the mean function from the my_math module can be referenced by my_mean and the mean function from statistics can be referenced by mean
