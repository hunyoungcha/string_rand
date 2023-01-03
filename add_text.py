#hwp의 받아온 text를 필요한 부분만 정리해서 all_data.txt에 저장하는 코드

import os
import hwp_text as ht

from pprint import pprint
#파일 위치 및 리스트
path="rhksckf/"
file_list=os.listdir(path)


g=[]
user_dict={'name':'','obs':'','note':''}


#hwp의 받아온 텍스트를 name obs note의 프레임으로 만들어 temp.txt에 저장
def add_temp():
    stop=0
    temp=open('temp.txt', 'w', encoding='utf-8')
    for q in file_list:
        hwp_text=ht.get_hwp_text(path+q)
        f=hwp_text.split('\n')

        for i in range(5,len(f)):
            if f[i].isspace()==False:
                if '공결' in f[i] or '코로나' in f[i] or '(' in f[i]:
                    temp.write(f[i])
                    temp.write('공결\n')
                    i+=1
                else:
                    temp.write(f[i])
    temp.close()

#temp 에서 all_data로 기준에 맞는 값만 옮기는 함수
#중간 중간 관찰내용이 아니라 이름이 들어가 있는 경우가 많음 ,고쳐야함
def temp_data_cont():
    t=open('temp.txt','r', encoding='utf-8')
    data_list=t.readlines()
    t.close()
    
    tmp=[]
    for i in data_list:
        q=i.split('\n')[0]
        if len(q)>3:
            tmp.append(q)
    
    ad=open('all_data.txt','w', encoding='utf-8')
    for i in range(0,len(tmp),2):
        ad.write(tmp[i]+'\n')
    ad.close()
  


    # ad=open('all_data.txt','w', encoding='utf-8')
    # for i in range(1,len(data_list),3):
    #     ad.write(data_list[i])

temp_data_cont()