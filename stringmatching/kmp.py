from stringmatching.base import Base

class KnuthMorrisPratt(Base):
    def search(self, pattern, text, all=False):
        start = 0
        self.m = len(pattern)
        self.n = len(text)
        self.strong_border = self.__strong_border(pattern)
        if all:
            results = []
            limit = len(text) - len(pattern)
            stop = False
            while start < limit and not stop:
                result = self.__knuth_morris_pratt(pattern, text, start)
                if result is not None:
                    results.append(result)
                    start = result + 1
                else:
                    stop = True
            return results
        else:
            return [ self.__knuth_morris_pratt(pattern, text, start) ]

    def __knuth_morris_pratt(self, pat, text, start):
        '''
        Knuth-Morris-Pratt string search

        Args:
            pat (str): pattern to search for
            text (str): source in what the pattern should be searched
            start (str): position in text where search should be started
        '''
        i = start
        j = 0
        while i <= self.n - self.m:
            while j < self.m and pat[j] == text[i + j]:
                j += 1
            if j == self.m:
                return i
            i += j - self.strong_border[j]
            j = max(0, self.strong_border[j])

    def __strong_border(self, pat):
        '''
        Returns the strong border table

        Args:
            pat (str): pattern to search for
        '''
        strong_border = [ -1 ]
        t = -1
        for j in range(1, self.m + 1):
            while t >= 0 and pat[t] != pat[j - 1]:
                t = strong_border[t]
            t += 1
            if j == self.m or pat[t] != pat[j]:
                strong_border.append(t)
            else:
                strong_border.append(strong_border[t])
        return strong_border