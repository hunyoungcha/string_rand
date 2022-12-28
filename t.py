def str_list():
    f=[]
    d=open('all_data.txt','r', encoding='utf-8')
    k=d.readlines()
    for i in k:
        f.append(i)
    return f
