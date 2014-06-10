def __last_occ(pat, text, start):
    '''
    Sliding window text search with last occurrence table
    P. 41 in Algorithms on Strings, there the alg. is called Fast-Search

    Args:
        pat (str): pattern to search for
        text (str): source in what the pattern should be searched
        start (str): position in text where search should be started
    '''
    m = len(pat)
    n = len(text)

    def __last_occurence(pat, text):
        '''
        Returns the las occurrence table

        Args:
            pat (str): pattern to search for
            text (str): source in what the pattern should be searched
        '''
        last_occ = {}
        A = set(text) | set(pat)
        for a in A:
            last_occ[a] = m # initialized with the length of the pattern
        for k in range(0, m - 1):
            last_occ[pat[k]] = m - 1 - k
        return last_occ

    j = m - 1
    last_occ = __last_occurence(pat, text)
    while j < n:
        #start = j-m+1
        i = start+j-m+1
        if text[i:start+j+1] == pat:
            return i
        j += last_occ[text[j]]