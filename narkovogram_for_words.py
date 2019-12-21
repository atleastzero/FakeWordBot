import narkovogram

class Narkovogram_for_words(narkovogram.Narkovogram):
    """This class will specifically be used for generating fake words."""

    def __init__(self, order=3, word_list=None):
        super(Narkovogram_for_words, self).__init__(order)

        self.words_so_far = []

        if word_list is not None:
            for word in word_list:
                self.add_word(word)

    def add_word(self, word):
        """Deconstructs a real word and adds its components to the 
            Narkovogram"""

        # Constructs start and stop tokens appropriate for order of 
        #   Narkovogram    
        start = ""
        end = ""

        for _ in range(self.order):
            start   += "("
            end     += ")"
        
        word = start + word + end

        # Grabs key-value pairs based on chain order.
        for index in range(len(word)-1):
            if index + self.order < len(word):
                key = word[index: index + self.order]
                value = word[index + self.order]
                self.add_count(key, value)

    