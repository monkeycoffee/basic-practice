
# coding: utf-8

# In[13]:


def make_primes(n):
    """构造最大值小于n的素数列表"""
    
    #初始的素数列表
    primes = [2, 3]
    temp = primes[-1] + 2
    
    if n < temp:
        return primes

    for num in range(temp, n, 2):
        for i in primes:
            if num % i == 0:
                break
            elif i**2 > num:
                primes.append(num)
                break
    return primes

