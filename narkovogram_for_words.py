import narkovogram

class Narkovogram_for_words(narkovogram.Narkovogram):
    """This class will specifically be used for generating fake words."""

    def __init__(self, word_list=None, order=3):
        super(Narkovogram_for_words, self).__init__(order)

        self.words_so_far = []

        if word_list is not None:
            for word in word_list:
                self.add_word(word)
                self.words_so_far.append(word)

    def add_word(self, word):
        """Deconstructs a real word and adds its components to the 
            Narkovogram"""

        # Constructs start and stop tokens appropriate for order of 
        #   Narkovogram    
        start = ""
        end = ")"

        for _ in range(self.order):
            start += "("
        
        word = start + word + end

        # Grabs key-value pairs based on chain order.
        for index in range(len(word)-1):
            if index + self.order < len(word):
                key = word[index: index + self.order]
                value = word[index + self.order]
                self.add_count(key, value)

    def random_walk(self):
        old_letters = ""
        produced_word = ""

        for _ in range(self.order):
            old_letters += "("
        
        newest_letter = old_letters[self.order - 1]

        while newest_letter != ")":
            newest_letter = self.sample_next(old_letters)
            produced_word += newest_letter
            old_letters = old_letters[1:] + newest_letter

        return produced_word[:len(produced_word)-1]


def print_narkovogram(nark):
    print('word list: {}'.format(nark.words_so_far))
    print('narkovogram: {}'.format(nark))
    print('{} tokens, {} types'.format(nark.tokens, nark.types))

def tests():
    f = open("/usr/share/dict/words", "r")
    contents = f.read()
    words_list = contents.split("\n")
    f.close()
    test_nark = Narkovogram_for_words(words_list)
    print_narkovogram(test_nark)
    print(test_nark.random_walk())

if __name__ == "__main__":
    tests()    
    