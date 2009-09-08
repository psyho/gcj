'''
Created on Sep 3, 2009

@author: psyho
'''

letters = 'welcome to code jam'
letter_set = set(letters)
def count_occurences(line):
    line = [c for c in line if c in letter_set]
    if len(line) < len(letters):
        return 0
    return count_letter_occurences(line, 0, 0)
    
def count_letter_occurences(line, letter_idx, line_idx):
    if len(line)-line_idx < len(letters)-letter_idx:
        return 0
    if letter_idx >= len(letters):
        return 1
    count = 0
    for i in range(line_idx, len(line)):
        if line[i] == letters[letter_idx]:
            count += count_letter_occurences(line, letter_idx+1, i+1)
    return count % 10000

def main():
    N = int(raw_input())    
    for i in range(N):
        line = raw_input()
        print 'Case #%d: %04d' % (i+1, count_occurences(line))
    

if __name__ == '__main__':
    main()