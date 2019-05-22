#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import redis, pandas, requests

import io, json, glob, shutil, hashlib, zipfile

from bs4 import BeautifulSoup

from datetime import datetime
import pandas as pd  



# Init Redis

r = redis.Redis(host='localhost', port=6379, db=0)



# Scrape latest csv url from page

result = requests.get("https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx")



c = result.content
print (c)

bse = pd.read_csv(r'C:\Users\nitin\python_notes\03-Methods and Functions\CSV_FILES\EQ210519.CSV', sep=',')
print(type(bse))
bse.head()


for row in bse:
    CLOSE = bse['CLOSE']
    OPEN = bse['OPEN']
    bse['GAIN'] = (CLOSE - OPEN)*100/CLOSE
#    bse['SC_NAME'] = bse['SC_NAME']
#index = pd.Series(['0','1', '2', '3', '4', '5','6', '7', '8', '9', '10'])
sort=bse.nlargest(10,"GAIN")
sort
#for item, row in sort.iterrows():
#      print (row)
#sort[sort.apply(lambda row: row['SC_NAME'].startswith('I'),axis=1)]
#choice = input("Enter choice(KAMAN HSG/GALLISPAT/IBVENTURES/IDFSENSEXE/SABOO SODIUM/KILBURN ENGG/SPEL SEMICON/SHIVA TEXYAM/IBVENTUREPP/UFO):")
#bse[bse['SC_NAME'].str.contains('KAMAN HSG')]
choice = input("Enter choice(IDFCFBLD1/MOHIT INDUS/BABA ARTS/SMRUTHIORG/MACHINO PLAS/TCI DEVELP/ELDECO HOUS/KAMAN HSG/RELTD/ESAB INDIA):")
bse[bse['SC_NAME'].str.contains(choice)]
#sort['SC_NAME']


# In[ ]:





# In[ ]:




