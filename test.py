import math
import pandas as pd
import openpyxl

df = pd.read_excel('/run/media/soumi/Luna (HDD)/CF-0001/PSHS/Statistics/Module 1/SLG 3.0 Data set 3.1 DOH COVID Data Drop Case Information.xlsx') # can also index sheet by name or fetch all sheets
frequency = pd.value_counts(df.Age).to_frame().reset_index().sort_index().reset_index(drop=True)
freq_list = pd.value_counts(df.Age).to_frame().reset_index()['Age'].tolist()
# frequency.sort()

# num.sort() 
# print(f'\n{num}')



# fdt = pd.Series(num).value_counts().sort_index().reset_index().reset_index(drop=True)
# fdt.columns = ['Element', 'Frequency']
# print (fdt)

print(frequency)
print('\n\n\n\n\n\n\n\n')
print(freq_list)