
# coding: utf-8

# 判断101-200之间有多少个素数，并输出所有素数。

# In[2]:


cnt = 0
for num in range(101, 201, 2):
    is_prime = 1 #默认num是素数
    begin = 3
    end = num // begin
    while(begin <= end):
        if num % begin == 0:
            is_prime = 0 #说明num不是素数
            #print("num = %i, i = %i, num/i = %i" % (num, i, num/i))
            break
        begin += 2
        end = num // begin
    if is_prime == 1:
        cnt += 1
        print("num = %i " % num)


# In[11]:


cnt

