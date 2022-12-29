#hwp의 받아온 text를 필요한 부분만 정리해서 all_data.txt에 저장하는 코드

import olefile as ol
import os
import hwp_text as ht
import pandas as pd
from pprint import pprint
#파일 리스트 받아오기
path="rhksckf/"
file_list=os.listdir(path)



d=open('all_data.txt', 'a', encoding='utf-8')
for q in file_list:
    hwp_text=ht.get_hwp_text(path+q)
    f=hwp_text.split('\n')

    for i in range(6,len(f),3):
        if len(f[i])>5 and f[i][0].isalpha()==True:
            d.write(q+f[i])

# print(f[start])
# for i in hwp_text:
#     f.append(i)

d.close()

