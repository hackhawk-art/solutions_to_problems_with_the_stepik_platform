class TextHandler:
    def __init__(self, words=[], short_words=[], long_words=[]):
        self.words = words
        self.short_words = short_words
        self.long_words = long_words

    def add_words(self, text):
        for i in text.split():
            self.words.append(i)

    def get_shortest_words(self):
        for i in self.words:
            if len(i) == len(min(self.words, key=len)):
                self.short_words.append(i)
        return self.short_words

    def get_longest_words(self):
        for i in self.words:
            if len(i) == len(max(self.words, key=len)):
                self.long_words.append(i)
        return self.long_words

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())