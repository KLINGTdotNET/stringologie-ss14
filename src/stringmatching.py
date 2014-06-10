from enum import Enum,unique
import logging

from bm import __boyer_moore
from kmp import __knuth_morris_pratt
from last_occ import __last_occ
from mp import __morris_pratt
from naive import __naive

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
    if isinstance(algorithm, Algorithms):
        stop = False
        results = []
        start = 0
        limit = len(text) - len(pattern)
        while start < limit and not stop:
            if algorithm == Algorithms.naive:
                result = __naive(pattern, text, start)
            elif algorithm == Algorithms.last_occ:
                result = __last_occ(pattern, text, start)
            elif algorithm == Algorithms.morris_pratt:
                result = __morris_pratt(pattern, text, start)
            elif algorithm == Algorithms.knuth_morris_pratt:
                result = __knuth_morris_pratt(pattern, text, start)
            elif algorithm == Algorithms.boyer_moore:
                result = __boyer_moore(pattern, text, start)
            else:
                raise KeyError('Algorithm {}:{} is not implemented!'.format(algorithm.name, algorithm.value))
            if result is not None:
                start = result + 1
                results.append(result)
            if result is None or not all:
                stop = True
        if not results:
            print('Could not find pattern {}!'.format(pattern))
        return results
    else:
        logging.warn('The algorithm identifier must be from the Enum "Algorithms"!')
