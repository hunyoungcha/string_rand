import olefile as ol



count=220107

f= ol.OleFileIO('220107관찰일지.hwp')
encod_text=f.openstream('PrvText').read()
decod_text=encod_text.decode('UTF-16')
li=decod_text.split("\n")[2:]

d=open('all_data.txt', 'a', encoding='utf-8')
for i in li:
    d.write(f"{i.split('>')[1].split('<')[1]}\n")

