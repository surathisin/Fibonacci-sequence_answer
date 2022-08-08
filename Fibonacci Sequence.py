#!/usr/bin/env python
# coding: utf-8

# In[7]:


number = int(input("Please give input n"))
def fibonacci(n):
     
    
    f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
     
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
     
print(fibonacci(number))


# In[ ]:




