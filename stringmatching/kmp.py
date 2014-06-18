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
            while start <= limit and not stop:
                #result = self.__knuth_morris_pratt(pattern, text, start)
                result = self.__kmp(text[start:], pattern)
                if result:
                    results += result
                    start = result[-1] + len(pattern)
                else:
                    stop = True
            return results
        else:
            # return self.__knuth_morris_pratt(pattern, text, start)
            return self.__kmp(text, pattern)

    def __kmp(self, string, word):
        word_length = len(word)
        string_length = len(string)

        offsets = []

        if word_length > string_length:
            return offsets

        prefix = self.compute_prefix(word)
        q = 0
        for index, letter in enumerate(string):
            while q > 0 and word[q] != letter:
                q = prefix[q - 1]
            if word[q] == letter:
                q += 1
            if q == word_length:
                offsets.append(index - word_length + 1)
                q = prefix[q - 1]
        return offsets

    def compute_prefix(self, word):
        word_length = len(word)
        prefix = [0] * word_length
        k = 0

        for q in range(1, word_length):
            while k > 0 and word[k] != word[q]:
                k = prefix[k - 1]

            if word[k + 1] == word[q]:
                k = k + 1
            prefix[q] = k
        return prefix

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
        n = self.n
        m = self.m
        strong_border = self.strong_border # access to class attributes is slow
        while i <= n - m:
            while j < m and pat[j] == text[i + j]:
                j += 1
            if j == m:
                return i
            i += j - strong_border[j]
            j = strong_border[j]

    def __strong_border(self, pat):
        '''
        Returns the strong border table

        Args:
            pat (str): pattern to search for
        '''
        m = self.m
        strong_border = [ -1 ]
        t = -1
        for j in range(1, m + 1):
            while t >= 0 and pat[t] != pat[j - 1]:
                t = strong_border[t]
            t += 1
            if j == m or pat[t] != pat[j]:
                strong_border.append(t)
            else:
                strong_border.append(strong_border[t])
        return strong_border