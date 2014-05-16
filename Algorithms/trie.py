"""A simple Trie prototype.
http://en.wikipedia.org/wiki/Trie
"""

import unittest

class Trie(object):
    """Trie Node.
    """
#TODO test performance on real dictionary - bwargh 500 MB of memory!
#TODO key is a string. Wouldn't it be better for it to be a character?
#TODO think/test performance
#TODO locality of reference
#TODO number of nodes

    def __init__(self):
        self._children = dict()
        self._length = 0
        self._valid = False
        
    def insert(self, key, debug=False):
        """Insert key in the trie."""
        if debug: print 'key', key
        if key == "":
            self._valid = True
            self._length += 1
            if debug: print 'leaf', self
            return 1
        else:
            child = self._children.setdefault(key[0], Trie())
            remaining = "" if len(key) == 1 else key[1:]
            n_new_words = child.insert(remaining, debug)
            self._length += n_new_words
            if debug: print 'up', self
            return n_new_words

    def is_valid(self):
        """Returns: True if this Trie node corresponds to a valid key."""
        return self._valid

    def remove(self, key):
        """Remove key from the trie."""
        pass

    def subtrie(self, key):
        """Returns: sub-trie corresponding to key, possibly None
        """
        if key == "":
            return self
        else:
            child = self._children.get(key[0], None)
            if child is not None: 
                remaining = "" if len(key) == 1 else key[1:]
                return child.subtrie(remaining)
            else:
                return None

    def traverse(self, results, word=""):
        '''Returns the list of valid words in the trie in lexicographical order. 
        '''
        if self.is_valid():
            results.append(word)
        #TODO would be better to have a sorted container?
        for key, child in sorted( self._children.iteritems() ):
            child.traverse(results, word+key)

    def iteritems(self):
        return self._children.iteritems()

    def __getitem__(self, key):
        """Returns child corresponding to key."""
        return self._children[key]

    def __contains__(self, key):
        return key in self._children

    def __len__(self):
        """Number of valid keys in the trie."""
        return self._length
        
    def __repr__(self):
        return "Trie {id},{length} -> {children}".format(
            id=hex(id(self)),
            length=self._length,
            children=",".join(self._children.keys())
            )

    def get_words(self):
        '''prints all words in the trie.
        #TODO words are not complete for sub-tries (no info about ancestors)
        '''
        words = []
        self.traverse(words)
        return words


def build_test_trie():
    """Returns: a small test trie."""
    trie = Trie()
    words = [
        "a",
        "b",
        "abron",
        "badminton",
        "bad",
        "bid"
        ]
    for word in words:
        trie.insert( word, debug=False)
    return trie

ttrie = build_test_trie()        


def build_dict_trie(nwords=1000, mod=1, filename='/usr/share/dict/words'):
    """Returns: A trie containing the words from a dictionary.

    Args:
      nwords    number of words to insert
      mod       number of words to skip between selected words
      filename  path to a file containing one word per line
    """
    trie = Trie()
    ifile = open(filename)
    nwinc = 0
    for iw, word in enumerate(ifile):
        word = word.rstrip().lower()
        if iw % mod:
            continue
        if nwinc == nwords:
            break
        trie.insert(word)
        nwinc += 1
    return trie

dtrie = build_dict_trie()

        
class TrieCase(unittest.TestCase):

    def test_insert_char(self):
        trie = Trie()
        trie.insert("c")
        self.assertIn("c", trie._children)

    def test_insert_word(self):
        trie = Trie()
        trie.insert("colin")
        self.assertIn("c", trie._children)
        self.assertIn("o", trie._children["c"]._children)

    def test_subtrie(self):
        trie = Trie()
        self.assertEqual(trie.subtrie(""), trie)
        trie.insert("colin")
        colin = trie.subtrie("colin")
        self.assertNotEqual(colin, None)
        self.assertTrue(colin.is_valid())
        coli = trie.subtrie("coli")
        self.assertNotEqual(coli, None)
        self.assertFalse(coli.is_valid())        
        zobi = trie.subtrie("zobi")
        self.assertEqual(zobi, None)

    def test_repr(self):
        trie = Trie()
        trie.insert("colin")
        representation = trie.__repr__()
        self.assertRegexpMatches(representation, r"^Trie\s\S+\s->\s.*$")

    def test_contains(self):
        trie = build_test_trie()
        self.assertIn('a', trie)
        self.assertNotIn('z', trie)

    def test_length(self):
        trie = build_test_trie()
        self.assertEqual(len(trie), 6)

if __name__ == "__main__":

    import pprint
    import sys

    unittest.main()

