"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    Our RandomWordFinder is nice, but we’ve received a new requirement: 
    sometimes, we’ll be provided with files that have blank lines, 
    as well as lines that start with a # symbol to make a comment.

For example, we could have a file like this:

# Veggies

kale
parsnips

# Fruits

apple
mango
When we work with this, we want it to return one of the actual foods, 
like “kale” or “apple”, but never to return the blank lines or comments.

We can’t just change the original Word Finder, though — our requirements 
have changed, so it would be unfair for users of that class to have this 
behavior suddenly change.

Make a subclass, SpecialWordFinder, that uses WordFinder, but changes needed 
parts so it can work. Try to do this so as little code as needed is duplicated.
"""

def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]


""" Reference Springboard module 18.4 Python OPP """