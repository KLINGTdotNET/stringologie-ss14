import stringmatching
import logging

def main():
    # configure logger
    log_format = '[%(levelname)s] (#%(lineno)s) %(filename)s->%(funcName)s>>> "%(message)s"'
    logging.basicConfig(format=log_format)
    algs = stringmatching.Algorithms
    result = stringmatching.search('a','abcaayrdfa', algs.naive, all=True)
    print(result)
    result = stringmatching.search('a','abcaayrdfa', algs.last_occ, all=True)
    print(result)
    result = stringmatching.search('a','abcaayrdfa', algs.morris_pratt, all=True)
    print(result)
    result = stringmatching.search('a','abcaayrdfa', algs.knuth_morris_pratt, all=True)
    print(result)
    result = stringmatching.search('a','abcaayrdfa', algs.boyer_moore, all=True)
    print(result)

if __name__ == '__main__':
    main()