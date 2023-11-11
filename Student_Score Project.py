#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing necessary libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("Studentexamscores.csv")


# In[5]:


df.head()


# In[7]:


df.describe().T


# In[8]:


df.info()


# In[10]:


df.isnull().sum()


# # Drop unnamed column

# In[21]:


df=df.drop("Unnamed: 0", axis = 1)
df.head()


# # Changing weekly study hours columns

# In[22]:


df["WklyStudyHours"]=df["WklyStudyHours"].str.replace("05-Oct","5-10")
df.head(10)


# # Gender Distribution

# In[39]:


plt.figure(figsize=(5,5))
ax=sns.countplot(data=df,x="Gender")
plt.title("Gender_Distribution")
ax.bar_label(ax.containers[0])        # for providing lables to the values since the values of males and females are so close.
plt.show()


# From the above chart we can analyze that count of females in a school is more as compare to males in the school

# In[29]:


gb=df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb)


# In[41]:


plt.figure(figsize=(4,4))
plt.title("Relationship between Students score and Parent's Education")
sns.heatmap(gb, annot = True)        # by using this annot function we can get values of the mean score in the heatmap as well
plt.show()


#  from the above chart we have concluded that there is huge impact on marks of their students for examples the parents who have
# done masters degree are getting more marks as compared to others.

# In[36]:


gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gb1)


# In[42]:


plt.figure(figsize=(4,4))
plt.title("Relationship between Parent's Marital Status and Student'Score")
sns.heatmap(gb1, annot= True)
plt.show()


# From the above chart we can analyze that there is negligible impact of Parent marital status on the marks of the 
# student. There is no huge difference
Now for detection outliers we are ploting box plot
# In[51]:


sns.boxplot(x="MathScore",data=df)

plt.figure(figsize=(4,4))
plt.show()


# from the above code we can anayze that maths has more outliers and maths is comparatively tough subject for students to 
# score good marks

# Now Ploting Marks of students according to distribution of ethnic groups

# In[55]:


# first of all we are finding the unique values inside the column of ethnic group column
print(df["EthnicGroup"].unique())


# # Distribution of Ethnic group

# In[73]:


# first of all we are finding the count of ethnic group by using the loc function of pandas.
GroupA = df.loc[(df["EthnicGroup"]== "group A")].count()
GroupB = df.loc[(df["EthnicGroup"]== "group B")].count()
GroupC = df.loc[(df["EthnicGroup"]== "group C")].count()
GroupD = df.loc[(df["EthnicGroup"]== "group D")].count()
GroupE = df.loc[(df["EthnicGroup"]== "group E")].count()


l=['group A','group B','group C','group D','group E']
mlist=[GroupA["EthnicGroup"],GroupB["EthnicGroup"],GroupC["EthnicGroup"],GroupD["EthnicGroup"],GroupE["EthnicGroup"]]
plt.title("Distribution of Ethnic Groups")
plt.pie(mlist,labels=l,autopct="%1.2f%%") # this autopct is given to show the percentages  of the different groups
plt.show()


# In[75]:


ax=sns.countplot(data=df,x='EthnicGroup')
ax.bar_label(ax.containers[0])


# In[76]:


print(mlist)


# In[ ]:




