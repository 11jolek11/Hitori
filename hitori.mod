/*********************************************
 * OPL 22.1.1 Model
 * Author: Andrzej Dabrowski
 * Creation Date: Apr 30, 2023 at 5:36:57 PM
 *********************************************/



// int unique_values = 5;
// range range_unique_values = 1..unique_values;

// int size_of_board = 5;
// range range_board_size = 1..size_of_board;

// int search_depth = size_of_board - 1;
// range range_search_depth = 1..search_depth;

// Orginalna tablica:
//   [
//      [4, 8, 1,6, 3, 2, 5, 7],
//      [3, 6, 7, 2, 1, 6, 5, 4],
//      [2, 3, 4, 8, 2, 8, 6, 1],
//      [4, 1, 6, 5, 7, 7, 3, 5],
//      [7, 2, 3, 1, 8, 5, 1, 2],
//      [3, 5, 6, 7, 3, 1, 8, 4],
//      [6, 4, 2, 3, 5, 4, 7, 8],
//      [8, 7, 1, 4, 2, 3, 5, 6],
//  ];

// int board_state[range_unique_values][range_board_size][range_board_size] = 
// [
//     [
//         [0, 0, 0, 1, 0], 
//         [0, 0, 1, 0, 0], 
//         [0, 1, 0, 0, 0], 
//         [1, 0, 0, 0, 0], 
//         [0, 0, 0, 0, 0]
//         ], 
//     [
//         [1, 0, 1, 0, 0], 
//         [1, 0, 0, 0, 0], 
//         [1, 0, 1, 1, 0], 
//         [0, 0, 1, 0, 0], 
//         [1, 1, 0, 0, 1]
//         ], 
//     [
//         [0, 1, 0, 0, 0], 
//         [0, 0, 0, 1, 0], 
//         [0, 0, 0, 0, 0], 
//         [0, 0, 0, 0, 1], 
//         [0, 0, 0, 0, 0]
//         ],
//     [
//         [0, 0, 0, 0, 0], 
//         [0, 1, 0, 0, 0], 
//         [0, 0, 0, 0, 0], 
//         [0, 0, 0, 1, 0], 
//         [0, 0, 0, 0, 0]
//         ], 
//     [
//         [0, 0, 0, 0, 1], 
//         [0, 0, 0, 0, 1], 
//         [0, 0, 0, 0, 1], 
//         [0, 1, 0, 0, 0], 
//         [0, 0, 1, 1, 0]
//         ]
// ];


int unique_values = 2;
range range_unique_values = 1..unique_values;

int size_of_board = 2;
range range_board_size = 1..size_of_board;

int size_of_decision = size_of_board*3;
range range_decision_size = 1..size_of_decision;

int search_depth = size_of_board - 1;
range range_search_depth = 1..search_depth;


int board_state[range_unique_values][range_board_size][range_board_size] = 
[[[0, 1], [0, 0]], [[1, 0], [1, 1]]];



// decision 0 - white, 1 - black
dvar boolean decision[range_decision_size][range_decision_size];

dexpr float total_coverage = sum(i in range_decision_size) sum(j in range_decision_size) decision[i][j];

maximize total_coverage;

subject to {
    Ones_In_Left_Support_Columns:
    forall(y in range_board_size){
        sum(i in range_decision_size) decision[i][y] == size_of_decision;
    }

    Ones_In_Right_Support_Columns:
    forall(y in range_board_size){
        sum(i in range_decision_size) decision[i][y+2*size_of_board] == size_of_decision;
    }

    Ones_In_Upper_Support_Rows:
    forall(x in range_board_size){
        sum(i in range_decision_size) decision[x][i] == size_of_decision;
    }

    Ones_In_Bottom_Support_Rows:
    forall(x in range_board_size){
        sum(i in range_decision_size) decision[x+2*size_of_board][i] == size_of_decision;
    }

    Repeating_Numbers_in_Rows:
    forall(r in range_unique_values) {
        forall(x in range_board_size) {
            sum(i in range_board_size) decision[x+size_of_board][i+size_of_board]*board_state[r][x][i] <= 1;
        }
    }

    Repeating_Numbers_in_Columns:
    forall(r in range_unique_values) {
        forall(y in range_board_size) {
            sum(i in range_board_size) decision[i+size_of_board][y+size_of_board]*board_state[r][i][y] <= 1;
        }
    }
    
    Adjacent_Black_by_Row:
    forall(r in range_board_size) {
        forall(y in range_search_depth) {
            decision[r+size_of_board][y+size_of_board] + decision[r+size_of_board][y+1+size_of_board] <= 1;
        }
    }

    Adjacent_Black_by_Column:
    forall(c in range_board_size) {
        forall(x in range_search_depth) {
            decision[x+size_of_board][c+size_of_board] + decision[x+1+size_of_board][c+size_of_board] <= 1;
        }
    }
    // TODO: Add third constraint
}
