
# coding: utf-8

# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

# In[1]:


#初始的素数列表
prime_list = [2, 3, 5, 7, 11, 13]
#构造最大值不超过n的素数列表
def make_prime_list(n): # n > 13
    num = prime_list[-1] + 2
    while(num <= n):
        is_prime = 1
        i = 1; begin = prime_list[i]; end = num // begin
        while(begin <= end):
            if num % begin == 0:
                is_prime = 0
                break
            i += 1; begin = prime_list[i]; end = num // begin
        if is_prime == 1:
            prime_list.append(num)
        num += 2

make_prime_list(30)
