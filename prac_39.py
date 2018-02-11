
# coding: utf-8

# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

# In[1]:


def insert_func(lst, n):
    begin = 0
    end = len(lst) - 1
    while(begin < end):
        mid = (begin + end) // 2
        if n >= lst[mid]:
            begin = mid
        else:
            end = mid
    lst.insert(end, n)


# In[2]:


lst = [1, 2, 3]
insert_func(lst, 2.5)



