def __morris_pratt(pat, text, start):
    '''
    Morris-Pratt string search

    Args:
        pat (str): pattern to search for
        text (str): source in what the pattern should be searched
        start (str): position in text where search should be started
    '''
    i = start
    j = 0
    m = len(pat)
    n = len(text)

    def __border_table(pat):
        '''
        Version from page 76
        '''
        m = len(pat)
        bord = [ -1 ]
        t = -1
        for j in range(1, m + 1):
            while t >= 0 and pat[t] != pat[j-1]:
                t = bord[t]
            t += 1
            bord.append(t) # bord[j] = t
        return bord

    def __border_table_mp(pat):
        '''
        Alternative border function based on MP itself, that uses pat and text synonymous
        '''
        i = 1
        j = 0
        m = len(pat)
        bord = [ -1 for _ in range(0, m+1) ]
        print(bord)
        while i <= m:
            while i+j < m and pat[j] == pat[i+j]:
                if bord[i+j] == -1:
                    bord[i+j] = j
                j += 1
            if bord[i+j] == -1:
                bord[i+j] = j
            i += j-bord[j]
            j = max(0, bord[j])
        return bord

    bord = __border_table(pat)

    # mp-shift == j-bord[j]
    while i <= n-m:
        while j < m and pat[j] == text[i+j]:
            j += 1
        if j == m:
            return i
        i += j-bord[j]
        j = max(0, bord[j])