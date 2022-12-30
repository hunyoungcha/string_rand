#hwp의 받아온 text를 필요한 부분만 정리해서 all_data.txt에 저장하는 코드

import olefile as ol
import os
import hwp_text as ht
import re
from pprint import pprint
path="rhksckf/"
file_list=os.listdir(path)
#pattern
pattern = re.compile(r'[ㄱ-ㅣ가-힣]')

stop_point=0
#file open
d=open('test.txt', 'a', encoding='utf-8')


for q in file_list:
    if stop_point==3:
        break

    hwp_text=ht.get_hwp_text(path+q)
    g=[]
    f=hwp_text.split('\n')
    cnt=1
    for i in f:
        cnt+=1
        if len(i)>5 and i[0]!='(' :
            if cnt%2==0:
                g.append(i)

    d.write(q+'\n')
    d.writelines(g[2:])
    stop_point+=1


# for i in range(6,len(f),3):
#     if '공결' in f[i]:
#         i-=1
#         print('공결')
#     if len(f[i])>5 and f[i][0].isalpha()==True:
#         print(f[i])

# print(f[start])
# for i in hwp_text:
#     f.append(i)

d.close()

