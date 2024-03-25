#!/usr/bin/env python
# coding: utf-8

# In[1]:


umur = int(input('masukan umur anda: '))
tinggi = int(input('masukan tinggi anda: '))



if umur <=2:
   tarif = "dilarang masuk"
elif umur <=4 and tinggi <70:
    tarif = 30000
elif umur <=4 and tinggi >70:
    tarif =40000
elif umur <=7 and tinggi <120:
    tarif = 40000
elif umur <=7 and tinggi >120:
    tarif = 55000
elif umur <=10 and tinggi <150:
    tarif = 50000
elif umur <=10 and tinggi >150:
    tarif = 70000
elif umur >10:
    tarif = 80000
 
print("Tarif Anda" , tarif)


# In[ ]:




