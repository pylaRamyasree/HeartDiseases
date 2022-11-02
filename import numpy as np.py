import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
df =  pd.read_csv('heart.csv')
df.info()
df.shape
df.head()
df.tail()
df
df.describe().T
df["target"].value_counts() 
fig = df.target.value_counts().plot(kind = 'bar', color=["lightblue", 'lightgreen'])
fig.set_xticklabels(labels=['Has Heart disease', "Doesn't have heart disease"], rotation=0)
plt.title("heart disease values")
plt.ylabel("amount");
labels = "has heart disease", "doesnt have heart disease"
explode =(0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(df.target.value_counts(), explode=explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=60)
ax1.axis('equal')
plt.show()
df.sex.value_counts()
labels = "MALES", "FEMALES"
explode=(0,0)
fig1,ax1=plt.subplots()
ax1.pie(df.sex.value_counts(), explode=explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=60)
ax1.axis('equal')
plt.show()
fig = sns.countplot(x='target',data=df,hue='sex')
fig.set_xticklabels(labels=["doesnt have heart disease",'has heart disease'],rotation=0)
plt.legend(['females','males'])
plt.title("heart disease frequency for sex")