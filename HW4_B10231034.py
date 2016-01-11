
# coding: utf-8

# In[1]:

#1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')
    


# In[2]:

#2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    elif start > guess_me:
        print('oops')
        break
    start += 1


# In[4]:

#3
for value in [3,2,1,0]:
    print(value)


# In[5]:

#4
even = [num for num in range(10) if num %2 == 0]
even


# In[6]:

#5
squares = {key : key*key for key in range(10)}
squares


# In[7]:

#6
odd = [num for num in range(10) if num %2 == 1]
odd


# In[8]:

#7
for  thing in ('Got %s' % num for num in range(10)):
    print(thing)


# In[9]:

#8 
def good():
    return['Harry','Run','Hermione']

good()


# In[17]:

#9
def get_odds():
    for number in range(1, 10, 2):
        yield number
        
for count, number in enumerate(get_odds(),1):
    if count == 3:
        print("The third odd number is",number)
        break
            


# In[18]:

#10
def test(func):
    def new_func(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('end')
        return result
    return new_func

@test
def greeting():
    print("Greetings,Earthling")
    
greeting()


# In[20]:




# In[ ]:



