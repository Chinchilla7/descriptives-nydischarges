import researchpy as rp
import pandas as pd
from tableone import TableOne, load_dataset

df = pd.read_csv('')
df.columns

#Prints out descriptive information for DataFrame.
rp.codebook(df)

#getting descriptive of single/continuous variables
rp.summary_cont(df[['']])

#getting descriptive of categorical variables
rp.summary_cat(df[[]])

df_columns = ['Age', 'HR', 'Group', 'sBP', 'Smoke']
df_categories = ['Smoke', 'Group']
df_groupby = ['Smoke']
# df2['Vocation'].value_counts()
df_table1 = TableOne(df, columns=df_columns, 
    categorical=df_categories, groupby=df_groupby, pval=False)
print(df_table1.tabulate(tablefmt = "fancy_grid"))
df2_table1.to_csv('descriptive/example1/data/test2.csv')