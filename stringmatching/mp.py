from stringmatching.base import Base

class MorrisPratt(Base):
    def search(self, pattern, text, all=None):
        start = 0
        self.m = len(pattern)
        self.n = len(text)
        self.bord = self.__border_table(pattern)
        if all:
            results = []
            limit = len(text) - len(pattern)
            stop = False
            while start <= limit and not stop:
                result = self.__morris_pratt(pattern, text, start)
                if result is not None:
                    results.append(result)
                    start = result + len(pattern)
                else:
                    stop = True
            return results
        else:
            return [ self.__morris_pratt(pattern, text, start) ]

    def __morris_pratt(self, pat, text, start):
        '''
        Morris-Pratt string search

        Args:
            pat (str): pattern to search for
            text (str): source in what the pattern should be searched
            start (str): position in text where search should be started
        '''
        i = start
        j = 0
        n = self.n
        m = self.m
        bord = self.bord

        while i <= n - m:
            while j < m and pat[j] == text[i + j]:
                j += 1
            if j == m:
                return i
            i += j - bord[j]
            j = max(0, bord[j])

    def __border_table(self, pat):
        '''
        Version from page 76

        Args:
            pat (str): pattern to search for
        '''
        bord = [ -1 ]
        m = self.m
        t = -1
        for j in range(1, m + 1):
            while t >= 0 and pat[t] != pat[j - 1]:
                t = bord[t]
            t += 1
            bord.append(t)
        return bord

    def __border_table_mp(self, pat):
        '''
        Alternative border function based on MP itself, that uses pat and text synonymous

        Args:
            pat (str): pattern to search for
        '''
        i = 1
        j = 0
        m = self.m
        bord = [ -1 for _ in range(0, m + 1) ]
        while i <= m:
            while i + j < m and pat[j] == pat[i + j]:
                if bord[i + j] == -1:
                    bord[i + j] = j
                j += 1
            if bord[i + j] == -1:
                bord[i + j] = j
            i += j-bord[j]
            j = max(0, bord[j])
        return bord