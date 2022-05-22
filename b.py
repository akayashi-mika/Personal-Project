import math
import numpy as np

x = int(input('x = '))
y = math.floor(math.sqrt(x)) + 20

while x < y:
    x = x + 1
    a = y ** 2
  
print(a)