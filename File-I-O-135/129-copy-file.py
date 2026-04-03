#fresh copy:
with open('gitcmd','r') as file,\
    open('copiedgitcmd','w') as out:
    for line in file:
        if not line.strip() == "":
            out.write(line)
    file.seek(0)
    content = list(dict.fromkeys(line.strip() for line in file))
    out = ''.join(f"{l}\n" for l in content)
    print(out)
with open('gitcmd','r') as f:
    out = ''
    for l in f:
        if l.strip():
            out += f"{l}"
    print(out)
with open('gitcmd') as f:
    out = ''
    out = ''.join(l for l in f if l.strip())

print(out, end='')
"""most efficient"""
# with open("input.txt") as src, open("output.txt","w") as dst:
#     dst.writelines(line for line in src if line.strip())