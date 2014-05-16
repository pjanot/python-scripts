"""A simple Trie prototype.
http://en.wikipedia.org/wiki/Trie
"""

import unittest

class Trie(object):
    """Trie Node.
    """

#TODO implement magic methods

    def __init__(self):
        self._children = dict()
        self._length = 0
        self._valid = False

    def insert(self, key):
        """Insert key in the trie."""
        if key == "":
            self._valid = True
            self._length += 1
        else:
            child = self._children.setdefault(key[0], Trie())
            remaining = "" if len(key) == 1 else key[1:]
            child.insert(remaining)

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

    def __len__(self):
        """Number of valid keys in the trie."""
        
    def __repr__(self):
        return "Trie {id} -> {children}".format(
            id=hex(id(self)),
            children=",".join(self._children.keys())
            )
        

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
        zobi = trie.subtrie("zobi")
        self.assertEqual(zobi, None)

    def test_repr(self):
        trie = Trie()
        trie.insert('colin')
        representation = trie.__repr__()
        self.assertRegexpMatches(representation, '^Trie\s\S+\s->\s.*$')


if __name__ == "__main__":

    unittest.main()
