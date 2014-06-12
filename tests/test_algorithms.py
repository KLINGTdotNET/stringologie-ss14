import unittest
from stringmatching import stringmatching as sm

class TestAlgorithms(unittest.TestCase):
    '''
    Corner Cases:
    - pattern and/or text is empty
    - pattern is only character long
    - first and all occurences of the pattern for all search operations
    - pattern is longer than the text
    - pattern is not in text
    - pattern is as long as the text
    - pattern is the text
    '''

    def setUp(self):
        self.one_char = {
            'pattern': 'a',
            'text': 'abc'*3,
            'result': [0, 3, 6]
        }
        self.longer = {
            'pattern': 'ab'*10,
            'text': 'ab'*4,
            'result': []
        }
        self.not_in_text = {
            'pattern': 'Andreas',
            'text': 'Linz',
            'result': []
        }
        pass

    def test_search(self):
        alg = sm.Algorithms.naive
        # test for empty values
        pattern = 'some pattern'
        text = 'another useless text'
        self.assertRaises(ValueError, sm.search, *('', text, alg))
        self.assertRaises(ValueError, sm.search, *(pattern, '', alg))
        self.assertRaises(ValueError, sm.search, *(None, text, alg))
        self.assertRaises(ValueError, sm.search, *(pattern, None, alg))

    def test_naive(self):
        alg = sm.Algorithms.naive
        self.assertEqual(self.one_char['result'],
            sm.search(self.one_char['pattern'], self.one_char['text'], alg, True))
        self.assertEquals(self.longer['result'],
            sm.search(self.longer['pattern'], self.longer['text'], alg, True))
        self.assertEquals(self.not_in_text['result'],
            sm.search(self.not_in_text['pattern'], self.not_in_text['text'], alg, True))

    def test_last_occ(self):
        alg = sm.Algorithms.last_occ
        self.assertEqual(self.one_char['result'],
            sm.search(self.one_char['pattern'], self.one_char['text'], alg, True))
        self.assertEquals(self.longer['result'],
            sm.search(self.longer['pattern'], self.longer['text'], alg, True))
        self.assertEquals(self.not_in_text['result'],
            sm.search(self.not_in_text['pattern'], self.not_in_text['text'], alg, True))

    def test_morris_pratt(self):
        alg = sm.Algorithms.morris_pratt
        self.assertEqual(self.one_char['result'],
            sm.search(self.one_char['pattern'], self.one_char['text'], alg, True))
        self.assertEquals(self.longer['result'],
            sm.search(self.longer['pattern'], self.longer['text'], alg, True))
        self.assertEquals(self.not_in_text['result'],
            sm.search(self.not_in_text['pattern'], self.not_in_text['text'], alg, True))

    def knuth_morris_pratt(self):
        alg = sm.Algorithms.knuth_morris_pratt
        self.assertEqual(self.one_char['result'],
            sm.search(self.one_char['pattern'], self.one_char['text'], alg, True))
        self.assertEquals(self.longer['result'],
            sm.search(self.longer['pattern'], self.longer['text'], alg, True))
        self.assertEquals(self.not_in_text['result'],
            sm.search(self.not_in_text['pattern'], self.not_in_text['text'], alg, True))

    def boyer_moore(self):
        alg = sm.Algorithms.boyer_moore
        self.assertEqual(self.one_char['result'],
            sm.search(self.one_char['pattern'], self.one_char['text'], alg, True))
        self.assertEquals(self.longer['result'],
            sm.search(self.longer['pattern'], self.longer['text'], alg, True))
        self.assertEquals(self.not_in_text['result'],
            sm.search(self.not_in_text['pattern'], self.not_in_text['text'], alg, True))
