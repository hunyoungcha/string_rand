import os
#for path in pathlist:
res = []
path="C:\Users\차훈영\Desktop\python\string_rand\\rhksckf"
for root, dirs, files in os.walk(path):
    rootpath = os.path.join(os.path.abspath(path), root)
    for file in files:
        filepath = os.path.join(rootpath, file)
        res.append(filepath) 

    for result in res:
        filename = result[:-4]+ ".txt"
        output = '--output ' + '"' + filename + '"'
        result = '"' + result + '"'
        print("hwp5txt" + " " + output + " " + result)
        os.system("hwp5txt" + " " + output + " " + result)