'''
Created on Sep 8, 2009

@author: psyho
'''
from unittest import TestCase
from itertools import imap
from operator import mul

def minimum_product(a, b):
    a.sort()
    b.sort(reverse=True)
    return sum(imap(mul, a, b))

def main():
    T = int(raw_input())
    for i in xrange(T):
        n = int(raw_input())
        a = map(int, raw_input().split())
        b = map(int, raw_input().split())
        print 'Case #%d: %d' % (i+1, minimum_product(a, b))

if __name__ == '__main__':
    main()        

class MinimumProductTest(TestCase):
    
    def testExampleA(self):
        self.assertEqual(-25, minimum_product([1, 3, -5], [-2, 4, 1]))
        
    def testExampleB(self):
        self.assertEqual(6, minimum_product([1, 2, 3, 4, 5], [1, 0, 1, 0, 1]))