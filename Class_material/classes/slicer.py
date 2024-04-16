class Text_Slicer:
    def __init__(self, text: str):
        self.text = text

    def split(self):
        return self.text.split()

    def count_words(self):
        return len(self.split())

    def filter_words(self, words: list[str]):
        found_words = []
        for word in self.split():
            if word in words:
                found_words.append(word)
        return found_words

    def get_words_by_length(self, length: int):
        found_words = []
        for word in self.split():
            if len(word) >= length:
                found_words.append(word)
        return found_words


text = Text_Slicer('I went to the shop and bought some happy drinks')

print(text.count_words())
print(text.filter_words(['went', 'to']))
print(text.get_words_by_length(5))