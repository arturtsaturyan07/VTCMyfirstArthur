import re
def count_sentences(text, mynum):
    shablon = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
    res = shablon.split(text)
    ress = []
    for i in res:
        if '!' in i:
            ress.append(i[0:i.index('!') + 1].strip())
            ress.append(i[i.index('!') + 1:].strip())
        else:
            ress.append(i.strip())
    print(*[i for i in ress if len(i) > mynum], sep='\n')
count_sentences(input(), int(input()))