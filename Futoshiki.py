#MeiNa Xie
#Winnie Zheng

class block():
    def __init__(self):
        self.val = 0 # empty is 0 else 1-5
        self.constraints = [] # > < ^ v constraints + values it can't be
        self.domain = [i for i in range(1,6)]

def add_contraint(block_board, val, i, j):
    for k in range(5):
        block_board[k][j].contraints.append(val)
        block_board[i][k].constraints.append(val)

def find_next(block_board):
    var = None
    for i in range(5):
        for j in range(5):
            # TODO: find the index of next var to assign using MRV and Degree
    if var is None: # when all variable is assigned
        return True
            
def initialize(filename):
    f = open(file_name, 'r')
    board = [f.readline().strip('\n').strip(' ').split(' ') for _ in range(5)]
    block_board = [[block() for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            val = board[i][j]
            block_board[i][j].val = val
            if val != 0:
                block_board[i][j].domain = []
                add_constraint(block_board, val, i, j)
                                
    f.readline()
    lr_cons = f.readline().strip('\n').strip(' ').split(' ') for _ in range(5)]
    for i in range(5):
        for j in range(4):
            if lr_cons[i][j] != 0:
                if lr_cons[i][j] == '>':
                    # greater than right
                    block_board[i][j].constraints.append('>.')
                    # less than left
                    block_board[i+1][j].constraints.append('.>')
                if lr_cons[i][j] == '<':
                    # less than right
                    block_board[i][j].constraints.append('<.')
                    # greater than left
                    block_board[i+1][j].constraints.append('.<')
                    
    f.readline()
    ud_cons = f.readline().strip('\n').strip(' ').split(' ') for _ in range(5)]
    for i in range(5):
        for j in range(4):
            if ud_cons[i][j] != 0:
                if ud_cons[i][j] == '^':
                    # less than down
                    block_board[i][j].constraints.append('^.')
                    # greater than up
                    block_board[i][j+1].constraints.append('.^')
                if lr_cons[i][j] == 'v':
                    # greater than down
                    block_board[i][j].constraints.append('v.')
                    # less than up
                    block_board[i][j+1].constraints.append('.v')

    return block_board


filename = input("Filename: ")
board = initialize(filename)
index = find_next(board)
while index is not True:
    board[index[0]][index[1]].val = min(board[i][j].domain)
    board[index[0]][index[1]].domain = []
    index = find_next(board)

# TODO: output is in board, put into output file
    
                
    

