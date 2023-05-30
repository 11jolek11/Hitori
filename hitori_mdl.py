from docplex.mp.model import Model
from converter import convert
import numpy as np

# input: table filled with numbers from hitori problem
input = np.array(
            [
                [2, 1],
                [2, 2]
            ]
        )

mdl = Model(name="HitoriSolver")

unique_values = 2

size_of_board = 2

size_of_decision = size_of_board*3

search_depth = size_of_board - 1

board_state = convert(input)

# decison = mdl.binary_var_matrix([i for i in range(size_of_decision)], [p for p in range(size_of_decision)])

# expression = sum([decison[i][j] for i in range(len(decison)) for j in range(len(decison[0]))])

# decison = mdl.binary_var_matrix([i for i in range(size_of_decision)], [p for p in range(size_of_decision)])
decison = [[mdl.binary_var(name="C" + str(r) + "_" + str(c)) for c in range(size_of_decision)] for r in range(size_of_decision)]

expression = sum([decison[i][j] for i in range(len(decison)) for j in range(len(decison[0]))])

mdl.maximize(expression)

mdl.solve()


def support_columns(decison):
    total_sum = 0
    # Ones_In_Left_Support_Columns
    for y in range(size_of_board):
        for i in range(size_of_decision):
            total_sum += decison[i][y]

    # Ones_In_Right_Support_Columns
    for y in range(size_of_board):
        for i in range(size_of_decision):
            total_sum += decison[i][y-1+2*size_of_board]

    # Ones_In_Upper_Support_Rows
    for x in range(size_of_board):
        for i in range(size_of_decision):
            total_sum += decison[x][i]

    # Ones_In_Bottom_Support_Rows
    for x in range(size_of_board):
        for i in range(size_of_decision):
            total_sum += decison[x-1+2*size_of_board][i]
    
    if total_sum == size_of_decision*size_of_board*4:
        return 1
    else:
        return 0
    
def repeating_numbers(board_state):
    z_dim = len(board_state)
    y_dim = len(board_state[0])
    x_dim = len(board_state[0][0])
    for z in range(z_dim):
        for y in range(y_dim):
            for x in range(x_dim):
                pass
    

def adjacent_black(decision):
    pass

