import olefile as ol
import os

#파일 리스트 받아오기
path="rhksckf/"
file_list=os.listdir(path)



d=open('all_data.txt', 'a', encoding='utf-8')
for q in range(len(file_list)):
    f= ol.OleFileIO(path+file_list[q])
    try:
        encod_text=f.openstream('PrvText').read()
        decod_text=encod_text.decode('UTF-16')
        li=decod_text.split("\n")[2:]
        
        for i in li:
            if i.split('>')[1].split('<')[1] !='공결':
                d.write(f"{i.split('>')[1].split('<')[1]}\n")
    except:
        continue
d.close()

