class MinMaxWordFinder:
    def __init__(self):
        self.text = ''
        self.res_min = []
        self.res_max = []

    def add_sentence(self, t):
        self.text += (t) + ' '

    def shortest_words(self):
        self.res_min.extend(list(
            filter(lambda x: len(x) == len(min(sorted(self.text.split(), key=lambda x: len(x)))), self.text.split())))
        return sorted(self.res_min)
    res_min = []

    def longest_words(self):
        self.res_max.extend(list(
            filter(lambda x: len(x) == len(max(sorted(self.text.split(), key=lambda x: len(x)))), self.text.split())))
        return sorted(list(set(self.res_max)))
    res_max = []


finder = MinMaxWordFinder()
finder.add_sentence('')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

finder.add_sentence('bb cc    dd')
finder2 = MinMaxWordFinder()
print(' '.join(finder2.shortest_words()))
print(' '.join(finder2.longest_words()))

print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

finder2.add_sentence('bbb ccc    ddc')
finder.add_sentence('zzzz')
finder.add_sentence('p q r')

print(' '.join(finder2.shortest_words()))
print(' '.join(finder2.longest_words()))

print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

print(' '.join(finder2.shortest_words()))
print(' '.join(finder2.longest_words()))