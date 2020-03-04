# Loading Required Packages.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Loading All DataFrames With The Size of 100000 Rows.

df1 = pd.read_csv('H:/Masters/Thesis/2018/case_file/case_file.csv', nrows = 100000,  low_memory=False)
df2 = pd.read_csv('H:/Masters/Thesis/2018/event/event.csv', nrows = 100000,  low_memory=False)
# ************************* OWNER FILES STRT ****************************************************************
df3 = pd.read_csv('H:/Masters/Thesis/2018/owner/owner.csv', nrows=100000,  low_memory=False)
df4 = pd.read_csv('H:/Masters/Thesis/2018/owner_name_change/owner_name_change.csv', nrows=100000)

# ************************* CLASSIFICATION FILES STRT ****************************************************************
df5 = pd.read_csv('H:/Masters/Thesis/2018/classification/classification.csv', nrows = 100000,  low_memory=False)
df6 = pd.read_csv('H:/Masters/Thesis/2018/intl_class/intl_class.csv', nrows = 100000,  low_memory=False)
df7 = pd.read_csv('H:/Masters/Thesis/2018/us_class/us_class.csv', nrows=100000,  low_memory=False)

# ************************* THESE FILES LINKED TO 'CASEFILE'  ****************************************************************
df8 = pd.read_csv('H:/Masters/Thesis/2018/statement/statement.csv', nrows=100000,  low_memory=False)
df9 = pd.read_csv('H:/Masters/Thesis/2018/design_search/design_search.csv', nrows = 100000,  low_memory=False)
df10 = pd.read_csv('H:/Masters/Thesis/2018/prior_mark/prior_mark.csv', nrows=100000,  low_memory=False)
df11 = pd.read_csv('H:/Masters/Thesis/2018/foreign_app/foreign_app.csv', nrows = 100000,  low_memory=False)

# ************************* MADRID FILES STRT ****************************************************************
df12 = pd.read_csv('H:/Masters/Thesis/2018/madrid_intl_file/madrid_intl_file.csv', nrows=100000,  low_memory=False)
df13 = pd.read_csv('H:/Masters/Thesis/2018/madrid_event/madrid_event.csv', nrows = 100000,  low_memory=False)

# ************************* THESE FILES LINKED TO 'CASEFILE'  ****************************************************************
df14 = pd.read_csv('H:/Masters/Thesis/2018/correspondent_domrep_attorney/correspondent_domrep_attorney.csv', nrows = 100000,  low_memory=False)


df15 = pd.read_csv('H:/Masters/Thesis/2018/tm_app_daily/tm_app_daily.csv', nrows=100000,  low_memory=False)


#***************************************************** Working on Dataframe df1 *************************************************************

# Counting Null Values on Each Column in df1 'CASE_FILE'. 
tmp_df1 = df1.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df1 = df1[df1.columns[df1.isnull().sum() < 20000]]

# Displays descriptive stats for all columns in df1.
df1.describe()

#vewing Datatypes in a DataFrame.
df1.dtypes

#Changing Object type to DataTime Format
df1['cfh_status_dt'] = df1['cfh_status_dt'].astype('datetime64[ns]')
df1['renewal_dt'] = df1['renewal_dt'].astype('datetime64[ns]')
df1['registration_dt'] = df1['registration_dt'].astype('datetime64[ns]')
df1['filing_dt'] = df1['filing_dt'].astype('datetime64[ns]')

#KPI_01
graph1 = df1['filing_dt'].groupby([df1.filing_dt.dt.year]).agg('count').plot(figsize=(12, 10), linewidth=2.5, color='blue')

graph1 = df1['registration_dt'].groupby([df1.registration_dt.dt.year]).agg('count').plot(figsize=(12, 10), linewidth=2.5, color='green')

graph1 = df1['renewal_dt'].groupby([df1.renewal_dt.dt.year]).agg('count').plot(figsize=(12, 10), linewidth=2.5, color='red')

#KPI_02

reg_count =  df1['registration_no'].nunique()


#***************************************************** Working on Dataframe df2 *************************************************************

# Counting Null Values on Each Column in df2 'EVENT. 
tmp_df2 = df2.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df2 = df2[df2.columns[df2.isnull().sum() < 20000]]

#vewing Datatypes in a DataFrame.
df2.dtypes

#Changing Object type to DataTime Format
df2['event_dt'] = df2['event_dt'].astype('datetime64[ns]')

#KPI_01
df2.groupby(['event_dt']).agg('count').plot()

#KPI_02

df2.groupby('event_cd').nunique().plot()

#***************************************************** Working on Dataframe df3*************************************************************

# Counting Null Values on Each Column in df3. 
tmp_df3 = df3.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df3 = df3[df3.columns[df3.isnull().sum() < 20000]]





#***************************************************** Working on Dataframe df4 *************************************************************

# Counting Null Values on Each Column in df4. 
tmp_df4 = df4.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df4 = df4[df4.columns[df4.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df5 *************************************************************

# Counting Null Values on Each Column in df5. 
tmp_df5 = df5.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df5 = df5[df5.columns[df5.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df6 *************************************************************

# Counting Null Values on Each Column in df6. 
tmp_df6 = df6.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df6 = df6[df6.columns[df6.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df7 *************************************************************

# Counting Null Values on Each Column in df7. 
tmp_df7 = df7.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df7 = df7[df7.columns[df7.isnull().sum() < 20000]]



#***************************************************** Working on Dataframe df8 *************************************************************

# Counting Null Values on Each Column in df8. 
tmp_df8 = df8.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df8 = df8[df8.columns[df8.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df9 *************************************************************

# Counting Null Values on Each Column in df9. 
tmp_df9 = df9.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df9 = df9[df9.columns[df9.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df10 *************************************************************

# Counting Null Values on Each Column in df10. 
tmp_df10 = df10.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df10 = df10[df10.columns[df10.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df11 *************************************************************

# Counting Null Values on Each Column in df11. 
tmp_df11 = df11.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df11 = df11[df11.columns[df11.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df12 *************************************************************

# Counting Null Values on Each Column in df12. 
tmp_df12 = df12.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df12 = df12[df12.columns[df12.isnull().sum() < 20000]]

#***************************************************** Working on Dataframe df13 *************************************************************

# Counting Null Values on Each Column in df13. 
tmp_df13 = df13.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df13 = df13[df13.columns[df13.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df14 *************************************************************

# Counting Null Values on Each Column in df14. 
tmp_df14 = df14.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df14 = df14[df14.columns[df14.isnull().sum() < 20000]]


#***************************************************** Working on Dataframe df15 *************************************************************

# Counting Null Values on Each Column in df15. 
tmp_df15 = df15.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df15 = df15[df15.columns[df15.isnull().sum() < 20000]]

