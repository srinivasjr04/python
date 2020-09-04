#!/usr/bin/env python
# coding: utf-8

# In[41]:


number = int(input("Enter a 2 digit number : "))
print("Table of ",number)
tenspart = number // 10
onespart = number % 10
for i in range(1,11):
    tensporduct = str(tenspart * i)
    if len(tensporduct) < 2:
        tens = tensporduct.zfill(2)
    else:
        tens = tensporduct
    
    onesproduct = str(onespart * i)
    if len(onesproduct) < 2:
        ones = onesproduct.zfill(2)
    else:
        ones = onesproduct
    endtens = int(tens) 
    endones = int(ones[0])
    print(tens," ",ones," ","(",tens,"+",ones[0],")"," ",((endtens + endones)*10) + int(ones[1]))


# In[ ]:
# output

# Enter a 2 digit number : 88
# Table of  88
# 08   08   ( 08 + 0 )   88
# 16   16   ( 16 + 1 )   176
# 24   24   ( 24 + 2 )   264
# 32   32   ( 32 + 3 )   352
# 40   40   ( 40 + 4 )   440
# 48   48   ( 48 + 4 )   528
# 56   56   ( 56 + 5 )   616
# 64   64   ( 64 + 6 )   704
# 72   72   ( 72 + 7 )   792
# 80   80   ( 80 + 8 )   880

