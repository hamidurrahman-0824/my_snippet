with open('gitcmd','r') as f:
    lines = []
    for line in f:
        if not line.strip() == '':
            lines.append(line)
    print(''.join(line for line in lines))