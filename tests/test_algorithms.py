import unittest
from stringmatching import stringmatching as sm

class TestAlgorithms(unittest.TestCase):
    '''
    Corner Cases:
    - pattern and/or text is empty
    - pattern is only character long
    - first and all occurences of the pattern for all search operations
    - pattern is longer than the text and vice versa
    - pattern is not in text
    - pattern is as long as the text
    - pattern is the text
    '''

    def setUp(self):
        # prepare patterns and search text
        pass

    def test_search(self):
        alg = sm.Algorithms.naive
        # test for empty values
        self.assertRaises(ValueError, sm.search, *('', 'text', alg))
        self.assertRaises(ValueError, sm.search, *('pattern', '', alg))
        self.assertRaises(ValueError, sm.search, *(None, 'text', alg))
        self.assertRaises(ValueError, sm.search, *('pattern', None, alg))

    def test_naive(self):
        alg = sm.Algorithms.naive

    def test_last_occ(self):
        pass

    def test_morris_pratt(self):
        pass

    def knuth_morris_pratt(self):
        pass

    def boyer_moore(self):
        pass
