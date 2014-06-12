from stringmatching.base import Base

class Naive(Base):
    def search(self, pattern, text, all=False):
        start = 0
        if all:
            results = []
            limit = len(text) - len(pattern)
            stop = False
            while start <= limit and not stop:
                result = self.__naive(pattern, text, start)
                if result is not None:
                    results.append(result)
                    start = result + len(pattern)
                else:
                    stop = True
            return results
        else:
            return [ self.__naive(pattern, text, start) ]

    def __naive(self, pat, text, start=None):
        '''
        Naive sliding window algorithm

        Args:
            pat (str): pattern to search for
            text (str): source in what the pattern should be searched
            start (str): position in text where search should be started
        '''
        if not start:
            start = 0
        m = len(pat)
        n = len(text)
        i = start
        while i <= n - m:
            j = 0
            while j < m and pat[j] == text[i + j]:
                j += 1
            if j == m:
                return i
            i += 1