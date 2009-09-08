import re

def make_pattern(pattern):
    pattern = pattern.replace('(', '[').replace(')', ']') 
    pattern = '\A' + pattern + '\Z'
    return re.compile(pattern)

def main():
    L,D,N = map(int, raw_input().split())            
    words = [raw_input() for i in range(D)]
    patterns = [make_pattern(raw_input()) for i in range(N)]
    
    for idx, pattern in enumerate(patterns):
        count = 0
        for word in words:
            if pattern.match(word): count += 1
        print 'Case #%d: %d' % (idx+1, count)
        
    
if __name__ == '__main__':
    main()