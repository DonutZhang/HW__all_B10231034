
# coding: utf-8

# In[1]:

#3.1
years_list = [1980, 1981, 1982, 1983, 1984, 1985]
years_list


# In[2]:

#3.2
years_list[2]


# In[3]:

#3.3
sorted_years = sorted(years_list)
sorted_years[-1]


# In[47]:

#3.4 串列
thing = ['mozzarella','cin derella','salmonella']
thing


# In[48]:

#3.5 第一個字母改為大寫
thing[1] = thing[1].title()
thing


# In[49]:

#3.6改為大寫
thing[0] = thing[0].upper()
thing


# In[50]:

#3.7 del
thing.remove("salmonella")
thing


# In[53]:

#3.8
surprice = ['Groucho','Chico','Hapo']
surprice


# In[55]:

#3.9
surprice[-1] = surprice[-1].lower()
surprice


# In[58]:

surprice [-1] = surprice[-1][::-1]
surprice


# In[78]:

#3.10
e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
e2f


# In[71]:

#3.11
e2f['walrus']


# In[86]:

#3.12
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
f2e


# In[87]:

#3.13
f2e['chien']


# In[90]:

#3.14
set(e2f.keys())


# In[3]:

#3.15
life = {
    'animals':{
        'cats':[
            'Henri','Grumpy','Lucy'
            ],
        'octopi':{},
        'emus':{}
        },
    'palnt':{},
    'other':{}
       }
life


# In[9]:

#3.16
print(life.keys())
print(list(life.keys()))



# In[10]:

#3.17
print(life['animals'].keys())


# In[13]:

#3.18
print(life['animals']['cats'])


# In[ ]:



