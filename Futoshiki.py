#MeiNa Xie
#Winnie Zheng

class block():
    def __init__(self):
        self.val = 0 # empty is 0 else 1-5
        self.constraints = [] # > < ^ v constraints + values it can't be
        self.domain = [i for i in range(1,6)]

def add_constraint(block_board, val, i, j):
    for k in range(5):
        block_board[k][j].constraints.append(val)
        block_board[i][k].constraints.append(val)

def reverse_constraints(block_board, val, i, j):
    #reverse the constraints when the board is inconsistent

'''
def find_next(block_board):
    var = None
    for i in range(5):
        for j in range(5):
            # TODO: find the index of next var to assign using MRV and Degree
    if var is None: return True # when all variable is assigned
'''
            
def initialize(filename):
    f = open(filename, 'r')
    board = [f.readline().strip('\n').strip(' ').split(' ') for _ in range(5)]
    block_board = [[block() for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            val = int(board[i][j])
            block_board[i][j].val = val
            if val != 0:
                block_board[i][j].domain = []
                add_constraint(block_board, val, i, j)
                                
    f.readline()
    lr_cons = [f.readline().strip('\n').strip(' ').split(' ') for _ in range(5)]
    for i in range(5):
        for j in range(4):
            if lr_cons[i][j] == '>':
                # greater than right
                block_board[i][j].constraints.append('>.')
                # less than left
                block_board[i][j+1].constraints.append('.>')
            if lr_cons[i][j] == '<':
                # less than right
                block_board[i][j].constraints.append('<.')
                # greater than left
                block_board[i][j+1].constraints.append('.<')
                    
    f.readline()
    ud_cons = [f.readline().strip('\n').strip(' ').split(' ') for _ in range(4)]
    for i in range(4):
        for j in range(5):
            if ud_cons[i][j] == '^':
                # less than down
                block_board[i][j].constraints.append('^.')
                # greater than up
                block_board[i+1][j].constraints.append('.^')
            if ud_cons[i][j] == 'v':
                # greater than down
                block_board[i][j].constraints.append('v.')
                # less than up
                block_board[i+1][j].constraints.append('.v')

    return block_board

def Futoshiki(board):
    index = find_next(board)
    if index is True:
        return board
    if len(board[i][j].domain) != 0:
        domain = sort(board[i][j].domain)
        for val in domain:
            board[index[0]][index[1]].val =  val# what if not consistent
            board[index[0]][index[1]].domain = []
            add_constraints(board, val, index[0], index[1])
            board = Futoshiki(board)
            if board != False:
                return board
    board[i][j].val = 0
    board[i][j].domain = domain
    reverse_constraint(board, val, index[0], index[1])
    return False
    # TODO: find a way to rewind if not consistent
    

filename = input("Filename: ")
board = initialize(filename)
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j].val, board[i][j].constraints)
    print()
                   
#output = Futoshiki(board)

# TODO: put into output file
    
                
    

