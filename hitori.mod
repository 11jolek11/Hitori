/*********************************************
 * OPL 22.1.1 Model
 * Author: Andrzej Dabrowski
 * Creation Date: Apr 30, 2023 at 5:36:57 PM
 *********************************************/

int unique_values = ...;
range range_unique_values = 1..unique_values;

int size_of_board = ...;
range range_board_size = 1..size_of_board;

int size_of_decision = size_of_board*3;
range range_decision_size = 1..size_of_decision;

int search_depth = size_of_board - 1;
range range_search_depth = 1..search_depth;

int board_state[range_unique_values][range_board_size][range_board_size] = ...;

dvar boolean decision[range_decision_size][range_decision_size];

dexpr float total_coverage = sum(i in range_decision_size) sum(j in range_decision_size) decision[i][j];

minimize total_coverage;

subject to {
    Ones_In_Left_Support_Columns:
    forall(y in range_board_size)
        sum(i in range_decision_size) decision[i][y] == size_of_decision;

    Ones_In_Right_Support_Columns:
    forall(y in range_board_size)
        sum(i in range_decision_size) decision[i][y+2*size_of_board] == size_of_decision;

    Ones_In_Upper_Support_Rows:
    forall(x in range_board_size)
        sum(i in range_decision_size) decision[x][i] == size_of_decision;

    Ones_In_Bottom_Support_Rows:
    forall(x in range_board_size)
        sum(i in range_decision_size) decision[x+2*size_of_board][i] == size_of_decision;

    Repeating_Numbers_in_Rows:
    forall(r in range_unique_values)
        forall(x in range_board_size)
            sum(i in range_board_size) (1-decision[x+size_of_board][i+size_of_board])*board_state[r][x][i] <= 1;

    Repeating_Numbers_in_Columns:
    forall(r in range_unique_values)
        forall(y in range_board_size)
            sum(i in range_board_size) (1-decision[i+size_of_board][y+size_of_board])*board_state[r][i][y] <= 1;
    
    Adjacent_Black_by_Row:
    forall(r in range_board_size)
        forall(y in range_search_depth)
            decision[r+size_of_board][y+size_of_board] + decision[r+size_of_board][y+1+size_of_board] <= 1;

    Adjacent_Black_by_Column:
    forall(c in range_board_size)
        forall(x in range_search_depth)
            decision[x+size_of_board][c+size_of_board] + decision[x+1+size_of_board][c+size_of_board] <= 1;

    Closed_Shapes:
    forall(n in 1..size_of_board-1){
        forall(y_pos in size_of_board+1..2*size_of_board){
            forall(x_pos in size_of_board+1..2*size_of_board){
				sum(p in 1..n+1) (decision[y_pos-1+p][x_pos+1+n-p]
				+ decision[y_pos-1+p][x_pos-1-n+p]
				+ decision[y_pos+1-p][x_pos+1+n-p] 
				+ decision[y_pos+1-p][x_pos-1-n+p]) <= n*4+4 - 1;
            }
          }
        }                                    
    }
