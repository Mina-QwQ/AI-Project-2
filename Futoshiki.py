#MeiNa Xie
#Winnie Zheng

class block():
    def __init__(self):
        self.val = 0 # empty is 0 else 1-5
        self.constraints = [] # > < ^ v constraints + values it can't be
        self.domain = [i for i in range(1,6)] #values it can be 

def add_constraint(block_board, val, i, j):
    for k in range(5):
        if val not in block_board[k][j].constraints:
            block_board[k][j].constraints.append(val)
        if val not in block_board[i][k].constraints:
            block_board[i][k].constraints.append(val)
        if val in block_board[k][j].domain:
            block_board[k][j].domain.remove(val)
        if val in block_board[i][k].domain:
            block_board[i][k].domain.remove(val)

def remove_values(board, i, j, values):
    for value in values:
        if value in board[i][j].domain:
            board[i][j].domain.remove(value)
            

def add_inequality_constraint(board, i, j):
    #if string type exists in constraint of board[i][j]?
    for c in board[i][j].constraints:
        if c == '>.' and board[i][j+1].val != 0:
            values_to_remove = [_ for _ in range(1,board[i][j+1].val+1)]
            remove_values(board, i, j, values_to_remove)
        elif c == '.>' and board[i][j-1].val != 0:
            values_to_remove = [_ for _ in range( board[i][j-1].val+1,6)]
            remove_values(board, i, j, values_to_remove)
        if c == '<.' and board[i][j+1].val != 0:
            values_to_remove = [_ for _ in range(board[i][j+1].val+1, 6)]
            remove_values(board, i, j, values_to_remove)
        elif c == '.<' and board[i][j-1].val != 0:
            values_to_remove = [_ for _ in range(1, board[i][j-1].val+1)]
            remove_values(board, i, j, values_to_remove)
        if c == '^.' and board[i+1][j].val != 0:
            values_to_remove =[_ for _ in range(board[i+1][j].val+1, 6)]
            remove_values(board, i, j, values_to_remove)
        elif c == '.^' and board[i-1][j].val != 0:
            values_to_remove =[_ for _ in range(1, board[i-1][j].val+1)]
            remove_values(board, i, j, values_to_remove)
        if c == 'v.' and board[i+1][j].val != 0:
            values_to_remove = [_ for _ in range(1, board[i+1][j].val+1)]
            remove_values(board, i, j, values_to_remove)
        elif c == '.v' and board[i-1][j].val != 0:
            values_to_remove = [_ for _ in range(board[i-1][j].val+1, 6)]
            remove_values(board, i, j, values_to_remove)

def check_consistency(board, val, row, col): 
    for i in range(len(board)):
        if board[row][i].val == val and i != col:
            return False
    for i in range(len(board)):
        if board[i][col].val == val and i != row:
            return False
    for c in board[row][col].constraints:
        if c == '>.':
            if board[row][col+1].val != 0 and board[row][col+1].val > board[row][col].val:
                return False
        if c == '.>':
            if board[row][col-1].val != 0 and board[row][col-1].val < board[row][col].val:
                return False
        if c == '<.':
            if board[row][col+1].val != 0 and board[row][col+1].val < board[row][col].val:
                return False 
        if c == '.<':
            if board[row][col-1].val != 0 and board[row][col-1].val > board[row][col].val:
                return False 
        if c == '^.':
            if board[row+1][col].val != 0 and board[row+1][col].val < board[row][col].val:
                return False
        if c == '.^':
            if board[row-1][col].val != 0 and board[row-1][col].val > board[row][col].val:
                return False
        if c == 'v.':
            if board[row+1][col].val != 0 and board[row+1][col].val > board[row][col].val:
                return False
        if c == '.v':
            if board[row-1][col].val != 0 and board[row-1][col].val < board[row][col].val:
                return False
    return True 

def find_next(block_board):
    #check minimum remaining value heuristic 
    min_domain = 6
    mrv = []
    for i in range(5):
        for j in range(5):
            if block_board[i][j].val == 0: #is the value unassigned?
                # TODO: find the index of next var to assign using MRV and Degree
                if len(block_board[i][j].domain) < min_domain:
                    mrv = [(i,j)]
                elif len(block_board[i][j].domain) == min_domain:
                    mrv.append((i,j))
    if len(mrv) == 0: #if board is complete
        return True
    elif len(mrv) == 1: 
        return mrv[0]
    #check degree heuristic of the units with same MRV
    #will stick with the first unit with degree constraint if there are multiple
    val = mrv[0]
    max_constraints = len(block_board[mrv[0][0]][mrv[0][1]].constraints)
    for i in range(1,len(mrv)):
        if len(block_board[mrv[i][0]][mrv[i][1]].constraints) < max_constraints:
            val = mrv[i]
            max_constraints = len(block_board[mrv[i][0]][mrv[i][1]].constraints)
    return val
            
def initialize(filename):
    f = open(filename, 'r')
    board = [f.readline().strip('\n').strip(' ').split(' ') for _ in range(5)]
    block_board = [[block() for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            val = int(board[i][j])
            block_board[i][j].val = val
            if val != 0:
                block_board[i][j].domain = [val]
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
    for i in range(5):
        for j in range(5):
            add_inequality_constraint(block_board, i, j)
    return block_board

def Futoshiki(board):
    index = find_next(board)
    if index is True:
        return board
    i,j = index[0], index[1]
    if len(board[i][j].domain) != 0:
        board[i][j].domain.sort()
        for val in board[i][j].domain:
            board[i][j].val =  val 
            #check if board is consistent 
            is_consistent = check_consistency(board, val, i, j)
            if is_consistent:
                sub_board = Futoshiki(board)
                if sub_board != False:
                    return sub_board
            #if not consistent, revert back to original board
            board[i][j].val = 0 
    return False

filename = input("Filename: ")
board = initialize(filename)
output = Futoshiki(board)

f = open("Output"+filename[5], 'w')
for i in range(len(board)):
    for j in range(len(board)):
        f.write(str(board[i][j].val) + ' ')
    f.write("\n")
f.close()