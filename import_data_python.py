#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 09:56:05 2017

@author: ankit
"""

"""
Reading Text file
"""
file = open('news.txt', 'r')
file.read()
file.closed
file.close()
file.closed


with open('news.txt','r') as file:
    print(file.readline())
    print(file.readline())
    
    
"""
Reading Flat File
"""
#numpy ,pandas

import numpy as np
mnist_data = np.loadtxt('titanic.csv', dtype=float, delimiter=',', comments='#')

titanic_data = np.genfromtxt('titanic.csv', dtype=None, delimiter=',', 
                             skip_header=1)

 
import pandas as pd
df = pd.read_csv('titanic.csv',sep=',')

"""
Matlab File
"""

from scipy.io import loadmat
x = loadmat('test.mat')
x


"""
Reading Excel File
"""
import pandas as pd
file = pd.ExcelFile('test.xlsx')
file.sheet_names
df1 = file.parse('sheet1')
df2 = file.parse('Sheet2')


df3 = file.parse(0)
df4 = file.parse(1)

"""
DataBase  Sqlite
"""
import sqlite3
conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("select * from employees")
rows = cur.fetchall()
for row in rows:
    print(row)
    

import pandas as pd    
df = pd.read_sql_query("select * from employees", conn)



"""
DataBase  MongoDb
"""
import pandas as pd
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test

df1 = pd.DataFrame(list(db.movie.find()))

data = list(db.person.find())
df2 = pd.DataFrame(data)

from pandas.io.json import json_normalize
df3 = json_normalize(data)



"""
Fetch Remote File
"""

html_url = 'http://www.google.com'
csv_url = 'https://vincentarelbundock.github.io/Rdatasets/csv/datasets/Titanic.csv'
json_url = 'https://raw.githubusercontent.com/ankit25587/test/master/test.json'


import requests
res = requests.get(html_url)
res.status_code
htmldata = res.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(htmldata, 'html.parser')
title = soup.find('title')
print(title.string)


res = requests.get(json_url)
json_data = res.json()
json_data['firstName']
json_data['address']['postalCode']

import pandas as pd
df =pd.read_csv(csv_url)



 ''' Space Location '''
url1 = 'http://api.open-notify.org/iss-now.json'
 ''' No of people in space'''
url2 = 'http://api.open-notify.org/astros.json'

 
loc = requests.get(url1)
loc1 = loc.json()
loc1['iss_position']['latitude'] 


astro = requests.get(url2)
astro1 = astro.json()
astro1['number']
