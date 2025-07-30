def word_dict(word):
    d = {}
    for c in word:
        d[c] = d.get(c, 0) + 1
    return d


x = word_dict('BEEgeek')['e']

print(x)