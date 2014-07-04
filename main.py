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
    text = None
    with open('resources/big.txt', 'r') as f:
        text = f.read()
    result = {}
    pattern = 'Boscombe Valley is a country district not very far from Ross, in Herefordshire. The largest landed proprietor in that part is a Mr. John Turner, who made his money in Australia and returned some years ago to the old country. One of the farms which he held, that of Hatherley, was let to Mr. Charles McCarthy, who was also an ex-Australian. The men had known each other in the colonies, so that it was not unnatural that when they came to settle down they should do so as near each other as possible. Turner was apparently the richer man, so McCarthy became his tenant but still remained'
    runs = 50
    for name in sm.algs:
        alg = sm.algs[name]
        print('Measuring time for "{}" algorithm.'.format(name))
        result[name] = {
            'min': maxsize,
            'max': 0
        }
        for i in range(1, runs):
            start = time.clock()
            sm.search(pattern, text, alg, False)
            end = time.clock()
            duration = end-start
            if duration < result[name]['min']:
                result[name]['min'] = duration
            if duration > result[name]['max']:
                result[name]['max'] = duration
    result['find'] = {
        'min': maxsize,
        'max': 0
    }
    for i in range(1, runs):
        start = time.clock()
        text.find(pattern)
        end = time.clock()
        duration = end-start
        if duration < result['find']['min']:
            result['find']['min'] = duration
        if duration > result['find']['max']:
            result['find']['max'] = duration
    pprint(result)
    with open('resources/pi_10million.txt', 'r') as f:
        text = f.read()
    result = {}
    for name in sm.algs:
        alg = sm.algs[name]
        print('Measuring time for "{}" algorithm.'.format(name))
        result[name] = {
            'min': maxsize,
                'max': 0
            }
        for i in range(1, 3):
            start = time.clock()
            sm.search('180986', text, alg, False)
            end = time.clock()
            duration = end-start
            if duration < result[name]['min']:
                result[name]['min'] = duration
            if duration > result[name]['max']:
                result[name]['max'] = duration
    pprint(result)

if __name__ == '__main__':
    main()
