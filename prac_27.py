
# coding: utf-8

# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# In[2]:


def output(s):
    l = len(s)
    if l == 0: #终止条件
        return
    print(s[-1]) #打印当前列表最后一个元素
    output(s[:-1]) #将排除最后一个元素后的列表带回函数进行递归

output([1, 2, 3])

