import pandas as pd

# creating & printing a series
# creating a simple series object
# a panda series = one dimensional array of data values
s  = pd.Series([42, 21, 7, 3.5])
print(s)



# creating & printing a dataframe
#  = two-dimensional labeled data structure, much like a full spreadsheet.
# The purpose of the Series and DataFrame structures is to facilitate data storage, access, and analysis
df = pd.DataFrame({'age': 18,
                   'name': ['Alice', 'Bob', 'Carl'],
                   'cardio': [60, 70, 80]})
print(df)



# selecting elements in df
print(df['age']) # by column
# selecting by index & slice
print(df[2:3])
# boolean indexing
print(df[df['cardio']>60]) # access larger values than 60 & in the cardio column
# selecting by Label
print(df.loc[:, 'name'])
# to print all rows from the cardio columns age & cardio



# modifying an existing dataframe
df['age'] = 16
print(s) # changing the age
# changing all but the first row of the age column using slicing & loc
df = pd.DataFrame({'age': 18,
                   'name': ['Alice', 'Bob', 'Carl'],
                   'cardio': [60, 70, 80]})
# excluding first row
df.loc[1:,'age'] = 16
print(df)
# overwriting old data & adding new data
df.loc[:,'friend'] = 'Alice'
print(df)
# simpler version:
df['friend'] = 'Alice'
print(df)
