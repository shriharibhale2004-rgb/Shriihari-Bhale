# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 16:28:43 2026

@author: shrih
"""
##dataframe using nested list
import pandas as pd
technologies=[("spark",20000,"30days"),
              ("pandas",30000,"40days")]
df=pd.DataFrame(technologies)
print(df)
####
#with labels and column name
column_name=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_name,index=row_label)
print(df)
####
#you can also asign custom
#data type to column
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas",
               "Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration ':['30day','40days','35days', '40days','60days',
                 '50days','55days'],
    'Discount':[11.8,23.7,13.4,15.7,12.5,25.4,18.4]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)
####
#convert all types to best possible
df2=df.convert_dtypes()
print(df2.dtypes)
##change all columns to same type
df=df.astype(str)
print(df.dtypes)
##change type for one or multiple columns
df=df.astype({"Fee": int,"Discount":float})
print(df.dtypes)
##convert data type for all column in a list
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes
###ignore error
df=df.astype({"Courses":int},errors="ignore")
df.dtypes
##generate error
df=df.astype({"Coueses":int},errors="raised")
###
#convert feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df["Discount"]=pd.to_numeric(df['Discount'])
df.dtypes
df=df.astype(str)
print(df.dtypes)
df["Fee"]=pd.to_numeric(df['Fee'])
df.dtypes
####
#create dataframe from dictionary
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop"],
    'Fee' :[20000,25000,26000],
    'Duration':['30day','40days','35days'],
    'Discount':[1000,2300,1500]
              }
df=pd.DataFrame(technologies)
df
##convert dataframe to csv
df.to_csv('data_file.csv')
###read
df=pd.read_csv('data_file.csv')
###
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days','35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_labels)
print(df)
#dataframe properties
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes
df.info
##asessing one column contents
df['Fee']
##asessing two column contents
cols=['Fee','Duration']
df[cols]
df[['Fee','Discount']]
##select certain rows asign in to anothe data frame
df2=df[6:]
df2=df[:6]
df2
###select certain cell  from column
df['Duration'][2]
##subtract specific value from column
df['Fee']=df['Fee']-500
df['Fee']
###describe data frame
#describe data fram all numeric value
df.describe()
#rename columns name using rename()method
df= pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})
#drop dataframe rows nd column
df=pd.DataFrame(technologies,index=row_labels)
df1=df.drop(['r1','r2'])
df1=df.drop(df.index[1])
df1=df.drop(df.index[[1,2]])
#delete rows by index range
df1=df.drop(df.index[2:])
#when ypu have defailt index for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3],axis=0)#it will delete row0 and row3
df1
df1=df.drop(range(0,2))#it will delete 0 and 1
df1
##droping of column
import pandas as pd
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
              })
df=pd.DataFrame(technologies)
print(df)

##drop column by name
df2=df.drop(['Fee'],axis=1)
print(df2)
##3explicttly using parameter name 'label'
df2=df.drop(labels=['Fee'],axis=1)
##alternate 
df2=df.drop(columns=['Fee'],axis=1)
###drop colummn by index
print(df.drop(df.columns[1],axis=1))
df= pd.DataFrame(technologies)
df.drop(df.columns[2],axis=1,inplace=True)
#column with labels
df=pd.DataFrame(technologies)
df2=df.drop(['Courses','Fee'],axis=1)
print(df2)
#
df= pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
#remove column from dataframe inplace
df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
df
##data frame iloc and loc
import pandas as pd
import numpy as np
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas",
               None,"Spark","Python"],
    'Fee' :[22000,25000,23000,24000,np.nan,25000,25000,22000],
    'Duration':['30day','50days','55days','40days','60days',
                '35day','','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
          })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df= pd.DataFrame(technologies,index=row_labels)
print(df)
#
df2=df.iloc[:,0:2]
df2
#
df2=df.iloc[0:2,:]
df2
##sclicing specigi row and column using iloc
df2=df.iloc[1:2,1:3]
df2
##
df2=df.iloc[:,1:3]
df2
###select rows for integer index
df2=df.iloc[2]

df2=df.iloc[[2]]
df2
#############
df2=df.iloc[[2,3,6]]#select rows by index lis
df2=df.iloc[1:5]#select rows by integerindex range
df2=df.iloc[:1]#select first row
df2=df.iloc[:3]#select first three row
df2=df.iloc[-1:]#select last row
df2=df.iloc[-3:]#sel
df2=df.iloc[::2]
df2=df.iloc[2::]

######
#Select rows by index Labels
df2=df.loc['r2']
df2=df.loc[['r2']]
df
df2=df.loc[['r1','r2','r6']]
df2=df.loc['r1':'r5']#including r5
#######
df2=df.loc['r1':'r5':2]#select alternate rows
###select multiple columns

df2 =df.loc[:,['Courses','Fee','Duration']]
#
df2=df.loc[:,['Courses','Fee','Discount']]
#
df2=df.loc[:,['Fee','Discount']]
##
df2=df.loc[:,'Duration':]
#
df2=df.loc[:,:'Duration']
#
df2=df.loc[:,::2]
############
#pandas data frame query
df2=df.query("Courses=='Spark'")
print(df2)
#not equal codition
df2=df.query("Courses !='Spark'")
####
#pandas add column to dataframe
import pandas as pd
technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Discount':[0.1,0.2,0,0.5,0.1]
          }
df=pd.DataFrame(technologies)
print(df)
#add on column
tutors=['Ram','Shyam','Ghanshyam','Ganesh','Ramesh']
df2=df.assign(Tutorsassigned=tutors)
print(df2)
#add multiple coiumns
MNCCompanies =['TATA','HCL',"INFOSYS",'GOOGLE','AMAZONE']
df2=df.assign(MnC=MNCCompanies,tutors=tutors)
df2
##
#derive new column from existing column
df=pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x:x.Fee* x.Discount/100)
print(df2)
#append column to existing Pandas Data frame
#add
df=pd.DataFrame(technologies)
df["MNCCompanies"]=MNCCompanies
print(df)
#add column at the specific position
df=pd.DataFrame(technologies)
df.insert(0,'Tutors',tutors)
###pndas rename with column
import pandas as pd
technologies = ({
  'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle",
             "Java"],
  'Fee' :[20000,25000,26000,22000,24000,21000,22000],
  'Duration':['30day', '40days' ,'35days', '40days', '60days', 
              '50days', '55days']
              })
df=pd.DataFrame(technologies)
#rename column
df.rename({'Courses':'Courses_list'},axis='columns',inplace=True)
print(df.columns)
#rename multiple column
df.rename(columns={'Courses':'Courses_list','Fee':'Courses_fee','Duration':'Courses_duration'},inplace=True)
print(df.columns)
df.columns
#quick get number of rows in df
rows_count=len(df.index)
rows_count
#
rows_count=len(df.axes[0])
rows_count
#
rows_count=len(df.axes[1])
rows_count
############
import pandas as pd
import numpy as np
data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]
      }
df=pd.DataFrame(data)

def add_4(x):
    return x + 4
df["B"]=df["B"].apply(add_4)
df["B"]
df=pd.DataFrame(data)
#apply to multiple columns 
df[['A','B']] = df[['A','B']].apply(add_4)
df
###########
#apply lambda function each column
df2=df.apply(lambda x : x + 4)
df2
#########
df=pd.DataFrame(data)
df["A"]=df["A"].apply(lambda x: x-2)
print(df)
##########
df=pd.DataFrame(data)
def add_2(x):
    return x+2 
df=df.transform(add_2)
print(df)
###########
df=pd.DataFrame(data)
df
df['A']=df['A'].map(lambda A: A/2)
print(df)
############
#using numpy function on single column
import numpy as np
df=pd.DataFrame(data)
df
df['A']=df['A'].apply(np.square)
print(df)
###########
#
df=pd.DataFrame(data)
df
df['B']=np.square(df['B'])
print(df)
############
#pandas groupby() with example
import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df=pd.DataFrame(technologies)
print(df)
#use groupby to compute the sum
df2=df.groupby(['Courses']).sum()
print(df2)
#########
#group by multiple columns
df=pd.DataFrame(technologies)
df2=df.groupby(['Courses','Duration']).sum()
print(df2)
########
#add index to the grouped data
#add row index to the group by result
df2=df.groupby(['Courses','Duration']).sum().reset_index()
print(df2)
##############
#pandas get column names from dataframe
import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas"],
    'Fee' :[22000,25000,23000,24000,26000],
    'Duration':['30days','50days','30days', None,np.nan],
    'Discount':[1000,2300,1000,1200,2500]
          }
df=pd.DataFrame(technologies)
print(df)
df.columns
#get the list of all column names from headers
column_headers=list(df.columns.values)
print("The Column Header :", column_headers)
#using list(df) to get the column names
column_header = list(df)
column_header
#################
#pandas shuffle dataframe rows
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day','40days','35days','40days','60days','50days','55days'],
    'Discount':[1000,2300,1500,1200,2500,2100,2000]
               }
df=pd.DataFrame(technologies)
print(df)
#pandas shuffle dataframe rows
#shuffle the dataframe rows and return all rows
df1=df.sample(frac=1)
print(df1)
df1=df.sample(frac=0.5)
print(df1)
###########
#create a new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)
#drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)
####################
#joins
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
print(df2)
#pandas join dataframe
df3=df1.join(df2, lsuffix="_left", rsuffix="right", how='inner')
print(df3)
###########
#pandas join by default it will join the table left join
df3=df1.join(df2, lsuffix="_left", rsuffix="right")
print(df3)
############
#pandas left join dataframe
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='left')
print(df3)
#pandas right join dataframe
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')
print(df3)
#############
#pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='inner')
print(df3)
#pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='left')
print(df3)
#pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='right')
print(df3)
#############
#pandas merge dataframe
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)

technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
#using pandas.merge()
df3=df.merge(df1,df2)
############
#using dataframe.merge
df3=df1.merge(df2)

import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                 'Fee': [25000,25200,24500,24900]})
data=[df,df1]
df2=pd.concate(data)
df2
#appending multiple dataframes
import pandas as pd
df = pd.DataFrame({'Courses': ["Spark","PySpark","Python","pandas"],
                    'Fee' : [20000,25000,22000,24000]})

df1 = pd.DataFrame({'Courses': ["Pandas","Hadoop","Hyperion","Java"],
                 'Fee': [25000,25200,24500,24900]})
df2 = pd.DataFrame({'Duration':['30days','40days','35days','50days']})
df3=pd.concate([df,df1,df2])
print(df3)
