'''
Created on Sep 3, 2009

@author: psyho
'''

class Node:
    def __init__(self, row, col, attitude):
        self.row = row
        self.col = col
        self.attitude = attitude
        self.flows_to = None
        self.gathers = []
        self._neighbors = None
        self.letter = None
    
    def neighbors(self, nodes):
        if self._neighbors:
            return self._neighbors
        neighbors = []
        if self.row > 0:
            neighbors.append(nodes[self.row-1][self.col])
        if self.col > 0:
            neighbors.append(nodes[self.row][self.col-1])
        if self.col+1 < len(nodes[self.row]):
            neighbors.append(nodes[self.row][self.col+1])
        if self.row+1 < len(nodes):
            neighbors.append(nodes[self.row+1][self.col])
        self._neighbors = neighbors
        return self._neighbors
    
    def neighbor_attitudes(self, nodes):
        return [neighbor.attitude for neighbor in self.neighbors(nodes)]
    
    def set_flows_to(self, nodes):
        neighbors = self.neighbors(nodes)
        neighbor_attitudes = self.neighbor_attitudes(nodes)
        
        if not(neighbors): return
        
        min_attitude = min(neighbor_attitudes)
        if min_attitude < self.attitude:
            for neighbor in neighbors:
                if neighbor.attitude == min_attitude:
                    self.flows_to = neighbor
                    neighbor.gathers.append(self)
                    break
    
    def set_gathered_letters(self, letter):
        self.letter = letter
        queue = self.gathers[:]        
        while queue:
            node = queue.pop()
            node.letter = letter
            queue += node.gathers
    
    def basin(self):
        node = self
        while node.flows_to:
            node = node.flows_to
        return node

def solve_board(attitudes):
    nodes = []
    for row in range(len(attitudes)):
        nodes.append([])
        for col in range(len(attitudes[row])):
            nodes[row].append(Node(row, col, attitudes[row][col]))
    for row in nodes:
        for node in row:
            node.set_flows_to(nodes)
    
    letter = ord('a')
    for row in nodes:
        for node in row:
            if not(node.letter):
                basin = node.basin()
                basin.set_gathered_letters(chr(letter))
                letter += 1
    
    letters = []
    for row in range(len(attitudes)):
        letters.append([])
        for col in range(len(attitudes[row])):
            letters[row].append(nodes[row][col].letter)
    
    return letters        
    
def main():
    T = int(raw_input())
    for i in range(T):
        H, W = map(int, raw_input().split())
        attitudes = []
        for j in range(H):
            attitudes.append(map(int, raw_input().split()))
        letters = solve_board(attitudes)
        print 'Case #%d:' % (i+1)
        for row in letters:
            print ' '.join(row)

if __name__ == '__main__':
    main()