from enum import Enum,unique
import logging

from bm import BoyerMoore
from kmp import KnuthMorrisPratt
from last_occ import LastOcc
from mp import MorrisPratt
from naive import Naive

@unique # ensure different values
class Algorithms(Enum):
    naive = 1
    last_occ = 2
    morris_pratt = 3
    knuth_morris_pratt = 4
    boyer_moore = 5

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
    if isinstance(algorithm, Algorithms):
        if algorithm == Algorithms.naive:
            naive = Naive()
            return naive.search(pattern, text, all)
        elif algorithm == Algorithms.last_occ:
            last_occ = LastOcc()
            return last_occ.search(pattern, text, all)
        elif algorithm == Algorithms.morris_pratt:
            morris_pratt = MorrisPratt()
            return morris_pratt.search(pattern, text, all)
        elif algorithm == Algorithms.knuth_morris_pratt:
            kmp = KnuthMorrisPratt()
            return kmp.search(pattern, text, all)
        elif algorithm == Algorithms.boyer_moore:
            bm = BoyerMoore()
            return bm.search(pattern, text, all)
        else:
            raise KeyError('Algorithm {}:{} is not implemented!'.format(algorithm.name, algorithm.value))
    else:
        logging.warn('The algorithm identifier must be from the Enum "Algorithms"!')
