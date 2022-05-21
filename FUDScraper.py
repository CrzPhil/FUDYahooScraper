#!/usr/bin/env python
# coding: utf-8

# In[21]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


# In[136]:


import numpy as np


# In[11]:


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


# In[151]:


URL = "https://finance.yahoo.com/"


# In[13]:


driver.get(URL)


# In[152]:


def getTrendingTickers():
    tickers = set()
    driver.get("https://finance.yahoo.com/trending-tickers")
    table = driver.find_element(By.TAG_NAME, "table")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        tickers.add(row.text.strip().split('\n')[0])
    return tickers


# In[158]:


def getFinancials(ticker):
    out = []
    c_url = URL + f"quote/{ticker}/financials?p={ticker}"
    driver.get(c_url)
    try:
        header = driver.find_element(By.CLASS_NAME, "D\(tbhg\)")
        cols = header.find_elements(By.TAG_NAME, "span")
        table = driver.find_element(By.CLASS_NAME, "D\(tbrg\)")
        rows = table.find_elements(By.CSS_SELECTOR, "div[data-test='fin-row']")
    except Exception:
        return []
    out.append([col.text for col in cols])
    
    for row in rows:
        out.append(row.text)
        
    return out


# In[51]:


trending_tickers = getTrendingTickers()
print(trending_tickers)


# In[63]:


ticker = 'TSLA'
current_url = URL + f"quote/{ticker}?p={ticker}"


# In[64]:


current_url


# In[65]:


driver.get(current_url)


# In[127]:


header = driver.find_element(By.CLASS_NAME, "D\(tbhg\)")


# In[129]:


cols = header.find_elements(By.TAG_NAME, "span")


# In[135]:


for col in cols:
    print(col.text)


# In[112]:


table = driver.find_element(By.CLASS_NAME, "D\(tbrg\)")


# In[123]:


rows = table.find_elements(By.CSS_SELECTOR, "div[data-test='fin-row']")


# In[146]:


rows[2].text


# In[134]:


for row in rows:
    print(row.text.strip())
    print("#")


# In[155]:


getFinancials('TSLA')


# In[159]:


all_output = []
for ticker in trending_tickers:
    all_output.append(getFinancials(ticker))


# In[137]:


#driver.close()


# In[ ]:




