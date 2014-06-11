import stringmatching
import logging

def main():
    # configure logger
    log_format = '[%(levelname)s] (#%(lineno)s) %(filename)s->%(funcName)s>>> "%(message)s"'
    logging.basicConfig(format=log_format)
    algs = stringmatching.Algorithms
    pattern = 'a'
    text = 'abbacbac'
    result = stringmatching.search(pattern, text, algs.naive, all=True)
    print(result)
    result = stringmatching.search(pattern, text, algs.last_occ, all=True)
    print(result)
    result = stringmatching.search(pattern, text, algs.morris_pratt, all=True)
    print(result)
    result = stringmatching.search(pattern, text, algs.knuth_morris_pratt, all=True)
    print(result)
    result = stringmatching.search(pattern, text, algs.boyer_moore, all=True)
    print(result)

if __name__ == '__main__':
    main()