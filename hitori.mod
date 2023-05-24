/*********************************************
 * OPL 22.1.1 Model
 * Author: Andrzej Dabrowski
 * Creation Date: Apr 30, 2023 at 5:36:57 PM
 *********************************************/

int unique_values = 2;
range range_unique_values = 1..unique_values;

int size_of_board = 2;
range range_board_size = 1..size_of_board;

int size_of_decision = size_of_board*3;
range range_decision_size = 1..size_of_decision;

int search_depth = size_of_board - 1;
range range_search_depth = 1..search_depth;

//int support = 0;

int board_state[range_unique_values][range_board_size][range_board_size] = [[[0, 1], [0, 0]], [[1, 0], [1, 1]]];

dvar boolean decision[range_decision_size][range_decision_size];

dexpr float total_coverage = sum(i in range_decision_size) sum(j in range_decision_size) decision[i][j];

maximize total_coverage;

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
            sum(i in range_board_size) board_state[r][x][i] <= 1;
            // sum(i in range_board_size) decision[x+size_of_board][i+size_of_board]*board_state[r][x][i] <= 1;

    Repeating_Numbers_in_Columns:
    forall(r in range_unique_values)
        forall(y in range_board_size)
            sum(i in range_board_size) board_state[r][i][y] <= 1;
            // sum(i in range_board_size) decision[i+size_of_board][y+size_of_board]*board_state[r][i][y] <= 1;

    Adjacent_Black_by_Row:
    forall(r in range_board_size)
        forall(y in range_search_depth)
            decision[r+size_of_board][y+size_of_board] + decision[r+size_of_board][y+1+size_of_board] <= 1;

    Adjacent_Black_by_Column:
    forall(c in range_board_size)
        forall(x in range_search_depth)
            decision[x+size_of_board][c+size_of_board] + decision[x+1+size_of_board][c+size_of_board] <= 1;
            
      
    forall(n in 1..size_of_board-1){
        forall(y_pos in size_of_board+1..2*size_of_board){
            forall(x_pos in size_of_board+1..2*size_of_board){
				sum(p in 1..n+1) (decision[y_pos-1+p][x_pos+1+n-p] // ok 
				+ decision[y_pos-1+p][x_pos-1-n+p] //ok
				+ decision[y_pos+1-p][x_pos+1+n-p] 
				+ decision[y_pos+1-p][x_pos-1-n+p]) <= n*4+4 - 1;
//              sum(p in 1..n+1) decision[y_pos-1+p][x_pos+1+n-p] <= n+1 &&
//              sum(p in 1..n+1) decision[y_pos-1+p][x_pos-1-n+p] <= n+1 &&
//              sum(p in 1..n+1) decision[y_pos+1-p][x_pos+1+n-p] <= n+1 &&
//              sum(p in 1..n+1) decision[y_pos+1-p][x_pos-1-n+p] <= n+1;
            }
          }
        }                                    

//    forall(n in 1..size_of_board)
//        forall(y_pos in size_of_board..2*size_of_board)
//            forall(x_pos in size_of_board..2*size_of_board)
//                sum(x in 1..n) sum (y in 1..n) decision[y_pos + n - y + 1][x + x_pos] < n + 1 &&
//                sum(x in 1..n) sum (y in 1..n) decision[y_pos + n - y + 1 - n][x + x_pos + n] < n + 1 &&
//                sum(x in 1..n) sum (y in 1..n) decision[y_pos - y - 1 + n][x_pos - x + 1] < n+1 && 
//                sum(x in 1..n) sum (y in 1..n) decision[y_pos - y - 1 + n + n][x_pos - x + 1 + n] < n+1;


//	 forall(n in 1..size_of_board) {
//         forall(y_pos in size_of_board..2*size_of_board) {
//             forall(x_pos in size_of_board..2*size_of_board) {
//                 sum(x in 1..n) ( sum (y in 1..n) (decision[y_pos + n - y + 1][x + x_pos] + decision[y_pos + n - y + 1 - n][x + x_pos + n - 1] + decision[y_pos - y - 1 + n][x_pos - x + 1] + decision[y_pos - y - 1 + n + n][x_pos - x + 1 + n] ))<= 4*n+4;

//                 sum(x in 1..n) ( sum (y in 1..n) (decision[y_pos + n - y + 1][x + x_pos] + decision[y_pos + n - y + 1 - n][x + x_pos + n] + decision[y_pos - y - 1 + n][x_pos - x + 1] + decision[y_pos - y - 1 + n + n][x_pos - x + 1 + n] ))<= 4*n+4;
// }}}			
//                sum(x in 1..n) sum(y in 1..n) decision[y_pos + n - y+1][x + x_pos] + decision[y_pos + n - y + 1 - n][x + x_pos + n] +decision[x + x_pos + n][y_pos + n - y + 1 + n]+ decision[x + x_pos][y_pos + n - y + 1] <= 4*n+4;
}