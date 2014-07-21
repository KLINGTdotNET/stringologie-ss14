from stringmatching.base import Base
from collections import defaultdict

class KnuthMorrisPratt(Base):
    def search(self, pattern, text, all=False):
        start = 0
        self.table = self.__compute_table(pattern)
        if all:
            results = []
            limit = len(text) - len(pattern)
            stop = False
            while start <= limit and not stop:
                result = self.__kmp(text, pattern, start)
                if result is not None:
                    results.append(result)
                    start = result + len(pattern)
                else:
                    stop = True
            return results
        else:
            return self.__kmp(text, pattern, start)

    def __kmp(self, text, pattern, start):
        n = len(text)
        m = len(pattern)
        i = start
        j = 0
        for i in range(start, n):
            j = self.table[text[i]][j]
            if j >= m:
                break
        if j == m:
            return i - m + 1

    def __compute_table(self, pattern):
        # sedgewick 768
        m = len(pattern)
        table = defaultdict(lambda: [0] * m)
        alphabet = set(pattern)
        table[pattern[0]][0] = 1            # init first match
        x = 0
        for i in range(1, m):
            for a in alphabet:
                table[a][i] = table[a][x]   # copy mismatch cases
            table[pattern[i]][i] = i+1      # set match case
            x = table[pattern[i]][x]        # update restart state
        return table
