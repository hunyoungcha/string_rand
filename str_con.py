#all_data.txt에서 받아온 데이터를 list화 시켜서 재조립하는 코드

import random

f=[]
d=open('all_data.txt','r', encoding='utf-8')
k=d.readlines()
for i in k:
    f.append(i.replace('\n',''))

def rand_str():
    q=random.randrange(0,len(f)-1)
    return f[q]

