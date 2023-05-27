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
