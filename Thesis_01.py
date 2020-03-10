#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Loading Required Packages.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno


# In[2]:


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


# # Working on Dataframe df1

# In[3]:


#visulization of NULL values
sns.heatmap(df1.isnull(), cbar=False)


# In[12]:


#In Otherform of  Visulization of Null Values
msno.matrix(df1)


# In[13]:


#heatmap of null values
msno.heatmap(df1)


# # Removing Null Columns Which are havig more than 20%

# In[5]:


# Counting Null Values on Each Column in df1 'CASE_FILE'. 
tmp_df1 = df1.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df1 = df1[df1.columns[df1.isnull().sum() < 20000]]


# # Visulization Of Removing Null Columns

# In[6]:


#visulization of NULL values
sns.heatmap(df1.isnull(), cbar=False)


# In[10]:


df1.head()


# In[16]:


#datatypes in df1
df1.dtypes


# In[104]:


#TYPECASTING Changing Object type to DataTime Format
df1['cfh_status_dt'] = df1['cfh_status_dt'].astype('datetime64')
df1['renewal_dt'] = df1['renewal_dt'].astype('datetime64[ns]')
df1['registration_dt'] = df1['registration_dt'].astype('datetime64')
df1['filing_dt'] = df1['filing_dt'].astype('datetime64[ns]')


# In[15]:


#TYPECASTING Changing int type to String Format
df1['mark_id_char'] = df1['mark_id_char'].astype('string')


# In[17]:


# Displays descriptive stats for all columns in df1.
df1.describe()


# In[18]:


#KPI_01
graph1 = df1['filing_dt'].groupby([df1.filing_dt.dt.year]).agg('count').plot(figsize=(12, 10), linewidth=2.5, color='blue')

graph1 = df1['registration_dt'].groupby([df1.registration_dt.dt.year]).agg('count').plot(figsize=(12, 10), linewidth=2.5, color='green')

graph1 = df1['renewal_dt'].groupby([df1.renewal_dt.dt.year]).agg('count').plot(figsize=(12, 10), linewidth=2.5, color='red')


# # Working on Dataframe df2

# In[20]:


#visulization of NULL values
sns.heatmap(df2.isnull(), cbar=False)


# In[22]:


# Displays descriptive stats for all columns in df2.
df2.describe()


# In[24]:


df2.head(5)


# In[31]:


#datatypes in df2
df2.dtypes


# In[105]:


#TYPECASTING Changing int type to String Format
df2['event_cd'] = df2['event_cd'].astype('string')
df2['event_type_cd'] = df2['event_type_cd'].astype('string')
df2['event_dt'] = df2['event_dt'].astype('datetime64')


# In[32]:


#KPI_01
df2.groupby(['event_dt']).agg('count').plot()


# In[35]:


#KPI_02

df2.groupby('event_cd').nunique().plot()


# # Working on Dataframe df3

# In[37]:


#visulization of NULL values
sns.heatmap(df3.isnull(), cbar=False)


# In[38]:


# Displays descriptive stats for all columns in df2.
df3.describe()


# In[39]:


#heatmap of null values
msno.heatmap(df3)


# In[41]:


# Counting Null Values on Each Column in df3. 
tmp_df3 = df3.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df3 = df3[df3.columns[df3.isnull().sum() < 20000]]


# In[42]:


#visulization of NULL values
sns.heatmap(df3.isnull(), cbar=False)


# In[45]:


# Displays descriptive stats for all columns in df2.
df3.describe()


# In[46]:


df3.head(5)


# In[47]:


#datatypes in df3
df3.dtypes


# In[49]:


#Changing Object type to DataTime Format
df3['own_addr_city'] = df3['own_addr_city'].astype('string')
df3['own_name'] = df3['own_name'].astype('string')
df3['own_addr_state_cd'] = df3['own_addr_state_cd'].astype('string')


# # Working on Dataframe df4

# In[50]:


#visulization of NULL values
sns.heatmap(df4.isnull(), cbar=False)


# In[51]:


# Displays descriptive stats for all columns in df2.
df4.describe()


# In[52]:


df4.head(5)


# In[53]:


#datatypes in df4
df4.dtypes


# In[54]:


#Changing Object type to DataTime Format
df4['own_name_change'] = df4['own_name_change'].astype('string')


# # Working on Dataframe df5

# In[55]:


#visulization of NULL values
sns.heatmap(df5.isnull(), cbar=False)


# In[56]:


# Counting Null Values on Each Column in df3. 
tmp_df5 = df5.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df5 = df5[df5.columns[df5.isnull().sum() < 20000]]


# In[57]:


#visulization of NULL values
sns.heatmap(df5.isnull(), cbar=False)


# In[58]:


# Displays descriptive stats for all columns in df5.
df5.describe()


# In[59]:


#datatypes in df5
df5.dtypes


# In[60]:


df5.head(5)


# In[106]:


#Changing Object type to DataTime Format
df5['class_status_dt'] = df5['class_status_dt'].astype('datetime64')


# # Working on Dataframe df6

# In[62]:


#visulization of NULL values
sns.heatmap(df6.isnull(), cbar=False)


# In[64]:


# Displays descriptive stats for all columns in df5.
df6.describe()


# In[65]:


df6.head(5)


# In[66]:


#datatypes in df6
df6.dtypes


# # Working on Dataframe df7

# In[72]:


#visulization of NULL values
sns.heatmap(df7.isnull(), cbar=False)


# In[75]:


# Displays descriptive stats for all columns in df5.
df7.describe()


# In[76]:


df7.head(5)


# In[77]:


#datatypes in df7
df7.dtypes


# # Working on Dataframe df8

# In[78]:


#visulization of NULL values
sns.heatmap(df8.isnull(), cbar=False)


# In[79]:


# Displays descriptive stats for all columns in df8.
df8.describe()


# In[83]:


#datatypes in df8
df8.dtypes


# In[84]:


df8.head(5)


# In[82]:


#Changing Object type to DataTime Format
df8['statement_type_cd'] = df8['statement_type_cd'].astype('string')
df8['statement_text'] = df8['statement_text'].astype('string')


# # Working on Dataframe df9

# In[85]:


#visulization of NULL values
sns.heatmap(df9.isnull(), cbar=False)


# In[86]:


# Displays descriptive stats for all columns in df9.
df9.describe()


# In[87]:


#datatypes in df9
df9.dtypes


# In[91]:


df9.head(5)


# # Working on Dataframe df10

# In[88]:


#visulization of NULL values
sns.heatmap(df10.isnull(), cbar=False)


# In[89]:


# Displays descriptive stats for all columns in df9.
df10.describe()


# In[93]:


#datatypes in df9
df10.dtypes


# In[92]:


df10.head(5)


# # Working on Dataframe df11

# In[95]:


#visulization of NULL values
sns.heatmap(df11.isnull(), cbar=False)


# In[96]:


# Counting Null Values on Each Column in df11. 
tmp_df11 = df11.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df11 = df11[df11.columns[df11.isnull().sum() < 20000]]


# In[97]:


#visulization of NULL values
sns.heatmap(df11.isnull(), cbar=False)


# In[98]:


# Displays descriptive stats for all columns in df9.
df11.describe()


# In[113]:


#datatypes in df9
df11.dtypes


# In[101]:


df11.head(10)


# In[110]:


pd.Timestamp.min


# In[112]:


#Changing Object type to DataTime Format

df11['for_appl_country_cd'] = df11['for_appl_country_cd'].astype('string')


# # Working on Dataframe df12

# In[114]:


#visulization of NULL values
sns.heatmap(df12.isnull(), cbar=False)


# In[115]:


# Counting Null Values on Each Column in df11. 
tmp_df12 = df12.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df12 = df12[df12.columns[df12.isnull().sum() < 20000]]


# In[116]:


#visulization of NULL values
sns.heatmap(df12.isnull(), cbar=False)


# In[117]:


# Displays descriptive stats for all columns in df9.
df12.describe()


# In[121]:


#datatypes in df12
df12.dtypes


# In[119]:


df12.head(10)


# In[120]:


#Changing Object type to DataTime Format
df12['mir_uspto_ref_no'] = df12['mir_uspto_ref_no'].astype('string')
df12['mir_registration_dt'] = df12['mir_registration_dt'].astype('datetime64')
df12['mir_renewal_dt'] = df12['mir_renewal_dt'].astype('datetime64')


# # Working on Dataframe df13

# In[122]:


#visulization of NULL values
sns.heatmap(df13.isnull(), cbar=False)


# In[124]:


# Displays descriptive stats for all columns in df9.
df13.describe()


# In[125]:


#datatypes in df13
df13.dtypes


# In[126]:


df13.head(10)


# In[129]:


#Changing Object type to DataTime Format
df13['mir_event_cd'] = df13['mir_event_cd'].astype('string')
df13['mir_event_dt'] = df13['mir_event_dt'].astype('datetime64')


# # Working on Dataframe df14

# In[131]:


#visulization of NULL values
sns.heatmap(df14.isnull(), cbar=False)


# In[133]:


# Counting Null Values on Each Column in df11. 
tmp_df14 = df14.isna().sum()

# Removing Columns Which Is having More than 20000 NULL Values in a Column.
df14 = df14[df14.columns[df14.isnull().sum() < 20000]]


# In[134]:


#visulization of NULL values
sns.heatmap(df14.isnull(), cbar=False)


# In[135]:


# Displays descriptive stats for all columns in df9.
df14.describe()


# In[136]:


df14.dtypes


# In[137]:


df14.head(5)


# In[139]:


#Changing Object type to DataTime Format
df14['caddr_1'] = df14['caddr_1'].astype('string')


# # Working on Dataframe df15

# In[141]:


#visulization of NULL values
sns.heatmap(df15.isnull(), cbar=False)


# In[142]:


df15.dtypes


# In[143]:


df15.head(5)


# In[144]:


#Changing Object type to DataTime Format
df15['tad_create_dt'] = df15['tad_create_dt'].astype('datetime64')
df15['tad_version_dt'] = df15['tad_version_dt'].astype('datetime64')


# In[ ]:




