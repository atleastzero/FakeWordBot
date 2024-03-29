import custom_errors
import random

class Narkovogram(dict):
    """This class creates a dictionary representation of a histogram used
        to generate markov chains."""

    def __init__(self, order):
        super(Narkovogram, self).__init__()

        self.types = 0
        self.tokens = 0
        self.order = order

    def add_count(self, key, value, count=1):
        """Increase frequency count of given key-value pair by given 
            count amount."""
        
        # Increases word frequency by count
        self.tokens += count
        
        # Checks if key exists in self
        try:
            sub_dict = self[key]
                
        # Runs if key did not already exist to create a new "sub_dict"
        #   (sub_dict is a dictionary of value-count pairs, count being 
        #   the number of occurences of key-value pairing)
        except:
            sub_dict = dict()
            sub_dict[value] = count
            self[key] = sub_dict
            self.types += 1
        
        # Runs if key did exist, using sub_dict
        else:

            # Similar to first check, checks if value exists in sub_dict
            try:
                sub_dict[value] += count
                self[key] = sub_dict

            # Runs if key existed, but not value for key
            except:
                appended_sub_dict = dict()
                appended_sub_dict[value] = count
                for inner_key, inner_value in self[key].items():
                    appended_sub_dict[inner_key] = inner_value
                self[key] = appended_sub_dict

    def frequency(self, group):
        """Given a key 'group', return the frequency of that group as a 
            whole. In other words, returns the sum of the key-value counts
            for a given key."""
        histogram = self[group]
        frequency = 0
        for _, value in histogram.items():
            frequency += value
        return value

    def sample_next(self, recent):
        """Given a recent addition to the random walk, randomly sample the 
            next addition."""
        try:
            histogram = self[recent]

            # 'Targets' an index in the range of 0 to frequency
            target = random.randrange(self.frequency(recent))
            # Dart 'searches for' target by iterating through values 
            dart = 0
            last_item = None
            for item, pair_count in histogram.items():
                last_item = item
                if dart <= target:  # if dart hasn't 'found' target
                    dart += pair_count
                else:               # if dart has 'found' target
                    return item
            if last_item == None:
                raise custom_errors.LastItemError
            return last_item
        except:
            raise custom_errors.NotEnoughContentError
