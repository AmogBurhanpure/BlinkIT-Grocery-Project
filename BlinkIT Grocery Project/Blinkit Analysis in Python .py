#!/usr/bin/env python
# coding: utf-8

#  ## **DATA ANALYSIS PYTHON PROJECT - BLINKIT ANALYSIS**

# ### **Import Libraries**

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# ### **Import  Raw Data**

# In[2]:


df = pd.read_csv("C:/Users/Amog/OneDrive/Desktop/BlinkIT Grocery Data (2).csv")


# ### **Sample Data**

# In[3]:


df.head(20)  # lTop 20 Row See


# ### **Sample Data**

# In[3]:


df.tail(20)  # last 15 Row See


# ### **Size of  Data**

# In[5]:


print("Size of Data:",df.shape)


# ### **Field info**

# In[6]:


df.columns


# ### **Data Types**

# In[7]:


df.dtypes


# ### **Data Cleaning**

# In[8]:


print(df["Item Fat Content"].unique())


# In[9]:


print(df['Item Fat Content'].unique())


# In[10]:


df['Item Fat Content'] = df['Item Fat Content'].replace({
    'LF': 'Low Fat',
    'low fat': 'Low Fat',
    'reg': 'Regular'
})


# In[11]:


print(df["Item Fat Content"].unique())


# ### **BUSINESS REQIREMENTS**

# ### **KPI's REQIREMENTS**

# In[12]:


#Total Sales 
total_sales = df['Sales'].sum()

#Average Sales
avg_sales = df['Sales'].mean()

#No of iteam Sold 
no_of_items_sold = df['Sales'].count()

#Average Ratings
avg_ratings = df['Rating'].mean()

#Display

print(f"Total Sales: ${total_sales:,.0f}")
print(f"Average Sales: ${avg_sales:,.0f}")
print(f"No of Items Sold:{no_of_items_sold:,.0f}")
print(f"Average Ratings: {avg_ratings:,.1f}")



# ### **CHARTS REQIREMENTS**

# ### **Total Sales by Fat Content**

# In[13]:


sales_by_fat = df.groupby('Item Fat Content') ['Sales'].sum()

plt.pie(sales_by_fat,labels = sales_by_fat.index,
        autopct = '%.0f%%',
        startangle = 90)

plt.title('Sales by Fat Content')
plt.axis('equal')
plt.show()
        


# ### **Total Sales by Item Type**

# In[14]:


sales_by_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
bars = plt.bar(sales_by_type.index,sales_by_type.values) #pass the  (X,y)

plt.xticks(rotation=90)   # Y axis Label   
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales By Item Type')


for bar in bars : 
    plt .text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
            f'{bar.get_height():,.0f}', ha='center', va='bottom',fontsize=8)  # Data Labels OR bar Chart Upper No Number (178,124 To 9,078) 
    
plt.tight_layout()
plt.show()


# ### **Fat Content by Outlet for Total Sales**

# In[15]:


grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped [['Regular','Low Fat']]


ax = grouped.plot(kind='bar',figsize=(8,5), title='Outlet Tier by Iteam Fat Content') # Char types And NAme of Chart
plt.xlabel('Outlet Loction Tier')
plt.ylabel('Total Sales')
plt.legend(title='Iteam Fat Content')
plt.tight_layout()
plt.show()


# ### **Total  Sales by Outlet Establishment**

# In[16]:


sales_by_year = df. groupby ('Outlet Establishment Year') ['Sales'].sum().sort_index()

plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index, sales_by_year.values,marker = 'o',linestyle= '-')

plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Outlet Establishment')

for x,y in zip(sales_by_year.index,sales_by_year.values):
    plt.text(x,y,f'{y:,.0f}',ha='center', va='bottom', fontsize=10)
    
plt.tight_layout()
plt.show()


# ### **Sales by Outlet Size**

# In[17]:


sales_by_size = df.groupby ('Outlet Size') ['Sales'].sum()

plt.figure(figsize=(4,4))
plt.pie(sales_by_size,labels=sales_by_size.index,autopct='%1.1f%%', startangle=90)
plt.title('Outlet Size')
plt.tight_layout()
plt.show()


# ### **Sales by Outlet Location**

# In[18]:


sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_by_location = sales_by_location.sort_values('Sales',ascending=False)

plt.figure(figsize=(8,3))  # Smaller height,enough width
ax = sns.barplot(x='Sales',y='Outlet Location Type', data=sales_by_location)

plt.title('Total Sales by outlet Location Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')

plt.tight_layout()  #Ensures layoout fites without scroll
plt.show()


# In[19]:


df['Item Type'].nunique()


# In[20]:


df.groupby('Outlet Type')['Sales'].mean()


# In[21]:


df.loc[df['Sales'].idxmax()]


# In[22]:


df.isnull().sum()


# In[24]:


df['Item Weight'].fillna(df['Item Weight'].mean(), inplace=True)


# In[25]:


df['Outlet Size'].value_counts()


# In[26]:


df.groupby('Item Type')['Rating'].mean()


# In[27]:


df.sort_values(by='Item Visibility', ascending=False).head(5)


# In[28]:


df['Item Fat Content'].value_counts()


# In[29]:


df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()


# In[30]:


top_5_sales = df.sort_values(by='Sales', ascending=False).head(5)


# In[ ]:




