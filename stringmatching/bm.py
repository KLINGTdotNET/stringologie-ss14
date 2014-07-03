from collections import defaultdict
from stringmatching.base import Base

class BMBase(Base):
    def _suffix(self, pattern):
        m = len(pattern)
        suff = [0]*m
        suff[m-1] = m
        g = m-1
        for i in range(m-2, -1, -1):
            if i > g and suff[i+m-1-f] != i-g:
                suff[i] = min(suff[i+m-1-f],i-g)
            else:
                f = i
                g = min(g,i)
                while(g >= 0 and pattern[g] == pattern[g+m-1-f]):
                    g = g-1
                suff[i] = f-g
        return suff

    def _weak_bm_shift(self, suff):
        m = len(suff)
        weakBM = [m]*m
        i = 0
        for j in range(m-2, -2, -1):
            if j == -1 or suff[j] == j+1:
                while i >= m - 1 - j:
                    weakBM[i] = m - 1 - j
                    i = i + 1
        for j in range(0, m-1):
            weakBM[m-1-suff[j]] = m-1-j
        return weakBM

    def _last_occurence(self, pattern):
        m = len(pattern)
        last_occ = defaultdict(lambda: m)
        for k in range(0,m-1):
            last_occ[pattern[k]] = m-1-k
        return last_occ

    def _border(self, pattern):
        j = 0
        t = -1
        m = len(pattern)
        bord = [0]*(m+1)
        bord[j] = t
        while j < m:
            j += 1
            while t >= 0 and pattern[t] != pattern[j-1]:
                t = bord[t]
            t += 1
            bord[j] = t
        return bord

class BoyerMooreGalil(BMBase):
    def search(self, pattern, text, all=False):
        self.memory = 0
        self.bm_shift = BMBase._weak_bm_shift(self, BMBase._suffix(self, pattern))
        self.last_occ = BMBase._last_occurence(self, pattern)
        self.bord = BMBase._border(self, pattern)
        start = 0
        if all:
            results = []
            limit = len(text) - len(pattern)
            stop = False
            while start <= limit and not stop:
                result = self.__bmg(pattern, text, start)
                if result is not None and result:
                    results += result
                    start = result[-1] + len(pattern)
                else:
                    stop = True
            return results
        else:
            return [ self.__bmg(pattern, text, start) ]

    def __bmg(self, pattern, text, start):
        results = []
        memory = self.memory
        bm_shift = self.bm_shift
        last_occ = self.last_occ
        bord = self.bord
        i = start
        n = len(text)
        m = len(pattern)
        while i <= n-m:
            j = m-1
            while j >= memory and pattern[j] == text[i+j]:
                j -= 1
            if j < memory:
                results.append(i)
                self.memory = bord[m]
                i += m - bord[m]
            else:
                self.memory = 0
                i += max(bm_shift[j if j>= 0 else 0], last_occ[text[i+j]]-m+j+1)
        return results


class BoyerMoore(BMBase):
    def search(self, pattern, text, all=False):
        self.bm_shift = BMBase._weak_bm_shift(self, BMBase._suffix(self, pattern))
        self.last_occ = BMBase._last_occurence(self, pattern)
        self.bord = BMBase._border(self, pattern)
        start = 0
        if all:
            results = []
            limit = len(text) - len(pattern)
            stop = False
            while start <= limit and not stop:
                result = self.__bm(pattern, text, start)
                if result is not None:
                    results.append(result)
                    start = result + len(pattern)
                else:
                    stop = True
            return results
        else:
            return [ self.__bm(pattern, text, start) ]

    def __bm(self, pattern, text, start):
        i = start
        n = len(text)
        m = len(pattern)
        bm_shift = self.bm_shift
        last_occ = self.last_occ
        while i <= n-m:
            j = m-1
            while j>=0 and pattern[j] == text[i+j]:
                j -= 1
            if j < 0:
                return(i)
            i += max(bm_shift[j if j >= 0 else 0], last_occ[text[i+j]]-m+j+1)