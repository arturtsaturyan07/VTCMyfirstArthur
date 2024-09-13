# import re
# def count_sentences(text):
#     a = re.compile(r'[A-Za-z0-9\s]+[.!?]')
#     k = a.findall(text)
#     return len(k)
#
# text = input().strip()
# sentence_count = count_sentences(text)
# print(sentence_count)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input())))