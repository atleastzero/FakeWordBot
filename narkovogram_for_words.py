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
            start   += "("
        
        word = start + word + end

        # Grabs key-value pairs based on chain order.
        for index in range(len(word)-1):
            if index + self.order < len(word):
                key = word[index: index + self.order]
                value = word[index + self.order]
                self.add_count(key, value)

def print_narkovogram(nark):
    print('word list: {}'.format(nark.words_so_far))
    print('narkovogram: {}'.format(nark))
    print('{} tokens, {} types'.format(nark.tokens, nark.types))

def tests():
    words = ["cat", "argument", "still", "camp"]
    print_narkovogram(Narkovogram_for_words(words))

if __name__ == "__main__":
    tests()    
    