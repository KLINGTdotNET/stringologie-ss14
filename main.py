#!/usr/bin/env python3

from stringmatching import stringmatching as sm
import logging
import time
from sys import maxsize
from pprint import pprint

def main():
    # configure logger
    log_format = '[%(levelname)s] (#%(lineno)s) %(filename)s->%(funcName)s>>> "%(message)s"'
    logging.basicConfig(format=log_format)
    algs = sm.Algorithms
    text = None
    with open('resources/big.txt', 'r') as f:
        text = f.read()
    result = {}
    for alg in algs:
        print('Measuring time for "{}" algorithm.'.format(alg.name))
        result[alg.name] = {
            'min': maxsize,
            'max': 0
        }
        result['find'] = {
            'min': maxsize,
            'max': 0
        }
        for i in range(1, 25):
            start = time.perf_counter()
            sm.search('gold', text, alg, False)
            end = time.perf_counter()
            duration = end-start
            if duration < result[alg.name]['min']:
                result[alg.name]['min'] = duration
            if duration > result[alg.name]['max']:
                result[alg.name]['max'] = duration
    for i in range(1, 25):
        start = time.perf_counter()
        text.find('gold')
        end = time.perf_counter()
        duration = end-start
        if duration < result['find']['min']:
            result['find']['min'] = duration
        if duration > result['find']['max']:
            result['find']['max'] = duration
    pprint(result)
    with open('resources/pi_10million.txt', 'r') as f:
        text = f.read()
    result = {}
    for alg in algs:
        if alg is not algs.boyer_moore:
            print('Measuring time for "{}" algorithm.'.format(alg.name))
            result[alg.name] = {
                'min': maxsize,
                'max': 0
            }
            for i in range(1, 3):
                start = time.perf_counter()
                sm.search('180986', text, alg, False)
                end = time.perf_counter()
                duration = end-start
                if duration < result[alg.name]['min']:
                    result[alg.name]['min'] = duration
                if duration > result[alg.name]['max']:
                    result[alg.name]['max'] = duration
    pprint(result)

if __name__ == '__main__':
    main()
