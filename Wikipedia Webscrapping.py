#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[5]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')



table = soup.find_all('table')[1]


# In[47]:


world_titles = table.find_all('th')


# In[49]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[53]:


import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

df


# In[56]:


column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[57]:


df

