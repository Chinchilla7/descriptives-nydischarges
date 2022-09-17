import researchpy as rp
import pandas as pd
from tableone import TableOne, load_dataset

df = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv')
df.columns

#Prints out descriptive information for DataFrame.
rp.codebook(df)

#getting descriptive of single/continuous variables
rp.summary_cont(df[['Facility Id','APR DRG Code', 'Type of Admission']])

#getting descriptive of categorical variables
rp.summary_cat(df[['Age Group','Facility Name']])

df['CCS Procedure Code']
df['Type of Admission'].value_counts()
# list of columns to be included in Table 1:
df_columns = ['CCS Procedure Code', 'APR DRG Code', 'Type of Admission']
# list of columns containing categorical variables:
df_categories = ['Type of Admission']
# a categorical variable for stratification:
df_groupby = ['Type of Admission']
# Creating an instance of TableOne with the input arguments:
df_table1 = TableOne(df, columns=df_columns, 
    categorical=df_categories, groupby=df_groupby, pval=False)
#print table onto terminal
print(df_table1.tabulate(tablefmt = "fancy_grid"))

df_table1.to_csv('new csv/prettytable.csv')