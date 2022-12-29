import olefile as ol


f= ol.OleFileIO('rhksckf/220107 관찰일지.hwp')
encod_text=f.openstream().read()
decod_text=encod_text.decode('UTF-16')
print(decod_text)