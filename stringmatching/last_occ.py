from stringmatching.base import Base
from collections import defaultdict

class LastOcc(Base):
    def search(self, pattern, text, all=False):
        start = 0
        self.m = len(pattern)
        self.n = len(text)
        self.last_occ = self.__last_occurence(pattern, text)
        if all:
            results = []
            limit = len(text) - len(pattern)
            stop = False
            while start < limit and not stop:
                result = self.__last_occ(pattern, text, start)
                if result is not None:
                    results.append(result)
                    start = result + 1
                else:
                    stop = True
            return results
        else:
            return [ self.__last_occ(pattern, text, start) ]

    def __last_occ(self, pat, text, start):
        '''
        Sliding window text search with last occurrence table
        P. 41 in Algorithms on Strings, there the alg. is called Fast-Search

        Args:
            pat (str): pattern to search for
            text (str): source in what the pattern should be searched
            start (str): position in text where search should be started
        '''
        j = self.m - 1
        while j < self.n:
            i = start + j - self.m + 1
            if text[i:start+j+1] == pat:
                return i
            j += self.last_occ[text[j]]

    def __last_occurence(self, pat, text):
        '''
        Returns the last occurrence table

        Args:
            pat (str): pattern to search for
            text (str): source in what the pattern should be searched
        '''
        last_occ = defaultdict(lambda: self.m) # saves initialization overhead by returning a default value when a non exisiting key is used
        for k in range(0, self.m - 1):
            last_occ[pat[k]] = self.m - 1 - k
        return last_occ