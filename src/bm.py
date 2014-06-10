def get_suff(pat):
    m = len(pat)
    g = m-1
    suff = [ 0 for _ in range(0, m)] # initialize
    suff[m-1] = m
    for i in reversed(range(0, m-1)):  # m-1 because the upper bound is exclusive
            if i > g and suff[i+m-1-f] < i-g:
                #suff[i] = min(suff[i+m-1-f], i-g)
                suff[i] = suff[i+m-1-f]
            else:
                if i < g:
                    g = i
                f = i
                while g >= 0 and pat[g] == pat[g+m-1-f]:
                    g -= 1
                suff[i] = f-g
    return suff

def get_weak_bm_shift(pat): # good suffix
    suff = get_suff(pat)
    m = len(pat)
    bm_shift = [m]*m
    for k in reversed(range(0, m)):
        if suff[k] == k+1:
            for i in range(0, m-k):
                if bm_shift[i] == m:
                    bm_shift[i] = m-1-k
    for k in range(0, m-1):
        bm_shift[m-1-suff[k]] = m-1-k
    return bm_shift

def get_bm_shift(pat, a):
    # returns bad_character shift table
    m = len(pat)
    bm_shift = {}
    for i in a:
        bm_shift[i] = m
    for i in range(0, m-1):
        bm_shift[pat[i]] = m-1-i
    return bm_shift

def __boyer_moore(pat, text, start):
    '''
    Boyer-Moore string search

    Args:
        pat (str): pattern to search for
        text (str): source in what the pattern should be searched
        start (str): position in text where search should be started
    '''
    m = len(pat)
    n = len(text)
    i = start
    a = set(pat) | set(text)
    weak_bm_shift = get_weak_bm_shift(pat) # good suffix table
    bm_shift = get_bm_shift(pat, a) # bad character table
    while i <= n-m:
        j = m-1
        while j >= 0 and pat[j] == text[i+j]:
            j -= 1
        if j < 0:
            return i
        else:
            i += bm_shift[text[i+j]] - m + 1
