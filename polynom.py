#mylist = eval(input()); print({k : [v1 for k1, v1 in mylist if k == k1] for k, v in mylist})
#text = input()
#import re; print(len(re.findall(r'[a-zA-Z]', text)), len((re.findall(r'[^!.?]*[!.?]{1,3}', text))), len(re.split(r'\s', text)))
#import re; print(sum(float(i) for i in re.findall(r"[+-]?\d+[.]?\d+", input())))
print(len(list(filter(lambda x: x.lower() in ['a', 'e', 'o', 'i', 'u', 'y'], input()))))