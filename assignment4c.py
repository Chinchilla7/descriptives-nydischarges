import researchpy as rp
import pandas as pd
from tableone import TableOne, load_dataset

df = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv')
df.columns

#Prints out descriptive information for DataFrame.
rp.codebook(df)

#getting descriptive of single/continuous variables
rp.summary_cont(df[['']])

#getting descriptive of categorical variables
rp.summary_cat(df[[]])

df_columns = ['Age Group',  'CCS Procedure Code', 'APR DRG Code', 'Type of Admission', 'Total Costs']
df_categories = ['Age Group', 'Type of Admission']
df_groupby = ['Age Group']
# df2['Vocation'].value_counts()
df_table1 = TableOne(df, columns=df_columns, 
    categorical=df_categories, groupby=df_groupby, pval=False)

print(df_table1.tabulate(tablefmt = "fancy_grid"))
df_table1.to_csv('new csv/prettytable.csv')