def __naive(pat, text, start=None):
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
            return i+j-1
        i += 1