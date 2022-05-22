from numpy import quantile
import pandas

list = [50, 60, 54, 39, 65, 46, 37, 39, 48, 72, 40, 47, 46, 41, 52, 38, 43, 55, 38, 49, 52, 45, 48, 45, 43, 54, 43, 55, 51, 40]
list_quantile = quantile(list, [.25,.5,.75])
# print(list)
print(list_quantile)