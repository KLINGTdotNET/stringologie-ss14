from enum import Enum,unique
import logging

from stringmatching.bm import BoyerMoore, BoyerMooreGalil
from stringmatching.kmp import KnuthMorrisPratt
from stringmatching.last_occ import LastOcc
from stringmatching.mp import MorrisPratt
from stringmatching.naive import Naive

algs = {
    'naive': Naive(),
    'last_occ': LastOcc(),
    'morris_pratt': MorrisPratt(),
    'knuth_morris_pratt': KnuthMorrisPratt(),
    'boyer_moore': BoyerMoore(),
    'boyer_moore_galil': BoyerMooreGalil()
}

def search(pattern, text, algorithm, all=False):
    '''
    Searches for the first or *all* occurrences of *pattern* in *text*, with the specified algorithm.

    Args:
        pattern (str): pattern which searched in text
        text (str): source in what the pattern should be searched
        all (bool): if True, search for all occurrences of pattern in text else return first occurrence or None
        algorithm (Algorithms): Enum value that specifies the algorithm to use
    '''
    if not pattern or not text:
        raise ValueError('Pattern or text is empty!')
    return algorithm.search(pattern, text, all)
