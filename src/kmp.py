def __knuth_morris_pratt(pat, text, start):
    '''
    Knuth-Morris-Pratt string search

    Args:
        pat (str): pattern to search for
        text (str): source in what the pattern should be searched
        start (str): position in text where search should be started
    '''
    def strong_border(pat):
        m = len(pat)
        strong_bord = [ -1 ]
        t = -1
        for j in range(1, m+1):
            while t >= 0 and pat[t] != pat[j-1]:
                t = strong_bord[t]
            t += 1
            if j == m or pat[t] != pat[j]:
                strong_bord.append(t)
            else:
                strong_bord.append(strong_bord[t])
        return strong_bord

    m = len(pat)
    n = len(text)
    i = start
    j = 0
    strong_bord = strong_border(pat)
    # kmp_shift == j-strong_bord[j]
    while i <= n-m:
        while j < m and pat[j] == text[i+j]:
            j += 1
        if j == m:
            return i
        i += j-strong_bord[j]
        j = max(0, strong_bord[j])