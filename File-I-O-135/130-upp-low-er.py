with open("repository_creation.txt",'r',encoding="utf-8") as f,\
    open('EMPTY.txt','w',encoding="utf-8") as out:
    for line in f:
        for ch in line:
            out.write(ch.upper())
