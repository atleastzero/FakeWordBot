class Narkovogram(dict):
    """This class creates a dictionary representation of a histogram used
        to generate markov chains."""

    def __init__(self, order):
        super(Narkovogram, self).__init__()

        self.types = 0
        self.tokens = 0
        self.order = order