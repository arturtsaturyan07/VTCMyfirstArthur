f = 'document1.docx'
with open(f, 'r+') as t:
    l = t.read()
    l.write(input())