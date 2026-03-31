#merge file linewese(f1l1f2l1f1l2f2l2...read write src dst new)
with open('gittroubleshots.txt','r',encoding="UTF-8") as src1:

    with open('repository_creation.txt','r',encoding="UTF-8") as src2:

        with open('merge.txt','w',encoding="utf-8") as dst:
            for l1,l2 in zip(src1,src2):
                dst.write(l1+l2)
src1 = open('gittroubleshots.txt','r',encoding="UTF-8")
src2 = open('repository_creation.txt','r',encoding="UTF-8")
with open('merge_file.txt','w',encoding='utf-8') as src:
    for l1,l2 in zip(src1,src2):
        l1 = l1.strip()
        l2 = l2.strip()
        src.write(l1.strip()+" " +l2.strip()+"\n")
src1.close()
src2.close()

##help
from itertools import zip_longest
src1 = open('gittroubleshots.txt','r',encoding="UTF-8")
src2 = open('repository_creation.txt','r',encoding="UTF-8")

with open('merge_file.txt','w',encoding='utf-8') as dst:
    for l1,l2 in zip(src1,src2):
        dst.write(l1.strip() + " " + l2.strip() + "\n")

src1.close()
src2.close()

with open('merge_file.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line, end="")
#
with open('gittroubleshots.txt',encoding="utf-8") as f1, \
     open('repository_creation.txt',encoding="utf-8") as f2, \
     open('merge_file.txt','w',encoding="utf-8") as out:

    for a,b in zip(f1,f2):
        out.write(a.strip() + " " + b.strip() + "\n")

with open('merge_file.txt',encoding="utf-8") as f:
    print(f.read())

#
with open('merge.txt','w',encoding='utf-8') as out, \
     open('gittroubleshots.txt',encoding='utf-8') as f1, \
     open('repository_creation.txt',encoding='utf-8') as f2:

    out.writelines(a.strip() + " " + b for a,b in zip(f1,f2))
#
from itertools import zip_longest

with open('merge.txt','w') as out, \
     open('gittroubleshots.txt') as f1, \
     open('repository_creation.txt') as f2:

    for a,b in zip_longest(f1,f2,fillvalue=""):
        out.write(a.strip()+" "+b.strip()+"\n")
#
with open('merge.txt','w') as out, \
     open('gittroubleshots.txt') as f1, \
     open('repository_creation.txt') as f2:

    for a,b in zip(f1,f2):
        line = a.strip()+" "+b.strip()
        print(line)
        out.write(line+"\n")

#
open("merge.txt","w").writelines(
    a.strip()+" "+b for a,b in zip(open("gittroubleshots.txt"), open("repository_creation.txt"))
)