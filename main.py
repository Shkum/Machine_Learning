import os
import pandas
a = os.path.abspath(os.getcwd())
print(a)
p = pandas.read_excel('trips_data.xlsx')
print(p.values[0])
# print(p.describe())
print(p.age)