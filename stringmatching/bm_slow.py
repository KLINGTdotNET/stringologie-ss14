from collections import defaultdict
from stringmatching.base import Base

class BoyerMoore(Base):
    def search(self, pattern, text, all=False):
        start = 0
        self.m = len(pattern)
        self.n = len(text)
        self.suffix = self.__get_suffix(pattern)
        self.weak_bm_shift = self.__get_weak_bm_shift(pattern)
        self.bm_shift = self.__get_bm_shift(pattern)
        if all:
            results = []
            limit = len(text) - len(pattern)
            stop = False
            while start <= limit and not stop:
                result = self.__boyer_moore(pattern, text, start)
                if result is not None:
                    results.append(result)
                    start = result + len(pattern)
                else:
                    stop = True
            return results
        else:
            return [ self.__boyer_moore(pattern, text, start) ]

    def __get_suffix(self, pat):
        '''
        Returns the suffix table

        Args:
            pat (str): pattern to search for
        '''
        m = self.m
        g = m - 1
        suff = [ 0 for _ in range(0, m) ] # initialize
        suff[m - 1] = m
        for i in reversed(range(0, m - 1)):  # m-1 because the upper bound is exclusive
            if i > g and suff[i + m - 1 - f] < i - g:
                suff[i] = suff[i + m - 1 - f]
            else:
                if i < g:
                    g = i
                f = i
                while g >= 0 and pat[g] == pat[g + m - 1 - f]:
                    g -= 1
                suff[i] = f-g
        return suff

    def __get_weak_bm_shift(self, pat):
        '''
        Returns the good suffix table

        Args:
            pat (str): pattern to search for
        '''
        m = self.m
        suffix = self.suffix
        bm_shift = [ m ] * m
        for k in reversed(range(0, m)):
            if suffix[k] == k + 1:
                for i in range(0, m - k):
                    if bm_shift[i] == m:
                        bm_shift[i] = m - 1 - k
        for k in range(0, m - 1):
            bm_shift[m - 1 - suffix[k]] = m - 1 - k
        return bm_shift

    def __get_bm_shift(self, pat):
        '''
        Returns the bad character shift table

        Args:
            pat (str): pattern to search for
        '''
        # returns bad_character shift table
        m = self.m
        bm_shift = defaultdict(lambda: m)
        for i in range(0, m - 1):
            bm_shift[pat[i]] = m - 1 - i
        return bm_shift

    def __boyer_moore(self, pat, text, start):
        '''
        Boyer-Moore string search

        Args:
            pat (str): pattern to search for
            text (str): source in what the pattern should be searched
            start (str): position in text where search should be started
        '''
        i = start
        n = self.n
        m = self.m
        wbs = self.weak_bm_shift
        bs = self.bm_shift
        while i <= n - m:
            j = m - 1
            while j >= 0 and pat[j] == text[i + j]:
                j -= 1
            if j < 0:
                return i
            else:
                i += max(wbs[j], bs[text[i + j]] - m + 1)
