import unittest
from stringmatching import stringmatching as sm

class TestAlgorithms(unittest.TestCase):
    '''
    Corner Cases:
    - pattern and/or text is empty
    - pattern is only character long
    - pattern is longer than the text
    - pattern is not in text
    - pattern is as long as the text
    - pattern is the text
    - first and all occurences of the pattern for all search operations
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
        self.same_length = {
            'pattern': 'abc'*3,
            'text': 'bcd'*3,
            'result': []
        }
        self.is_the_same = {
            'pattern': 'abc'*3,
            'text': 'abc'*3,
            'result': [0]
        }
        self.almost = {
            'pattern': 'a',
            'text': 'a'*1024,
            'result': [ _ for _ in range(1024) ]
        }

    def test_search(self):
        for alg in sm.Algorithms:
            pattern = 'some pattern'
            text = 'another useless text'
            self.assertRaises(ValueError, sm.search, *('', text, alg))
            self.assertRaises(ValueError, sm.search, *(pattern, '', alg))
            self.assertRaises(ValueError, sm.search, *(None, text, alg))
            self.assertRaises(ValueError, sm.search, *(pattern, None, alg))

    def test_corner_cases(self):
        for alg in sm.Algorithms:
            self.assertEqual(self.one_char['result'],
                sm.search(self.one_char['pattern'], self.one_char['text'], alg, True))
            self.assertEqual(self.longer['result'],
                sm.search(self.longer['pattern'], self.longer['text'], alg, True))
            self.assertEqual(self.not_in_text['result'],
                sm.search(self.not_in_text['pattern'], self.not_in_text['text'], alg, True))
            self.assertEqual(self.same_length['result'],
                sm.search(self.same_length['pattern'], self.same_length['text'], alg, True))
            self.assertEqual(self.same_length['result'],
                sm.search(self.same_length['pattern'], self.same_length['text'], alg, True))
            self.assertEqual(self.same_length['result'],
                sm.search(self.same_length['pattern'], self.same_length['text'], alg, True))
            self.assertEqual(self.same_length['result'],
                sm.search(self.same_length['pattern'], self.same_length['text'], alg, True))
            self.assertEqual(self.same_length['result'],
                sm.search(self.same_length['pattern'], self.same_length['text'], alg, True))
            self.assertEqual(self.is_the_same['result'],
                sm.search(self.is_the_same['pattern'], self.is_the_same['text'], alg, True))
            self.assertEqual(self.almost['result'],
                sm.search(self.almost['pattern'], self.almost['text'], alg, True))

    def test_all(self):
        for alg in sm.Algorithms:
            text = 'a'*1024+'b'
            self.assertEqual([ len(text)-1 ], sm.search('b', text, alg, True))
            text = ('a'*128+'b')*5
            result = [ x*128+x-1 for x in range(1,6) ]
            self.assertEqual(result, sm.search('b', text, alg, True))
            pattern = 'ac'
            text = ('abab'*1024+'ac')*5
            result = [ x*4*1024+2*(x-1) for x in range(1,6) ]
            self.assertEqual(result, sm.search(pattern, text, alg, True))
