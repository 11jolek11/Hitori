/*********************************************
 * OPL 22.1.1 Model
 * Author: Andrzej Dabrowski
 * Creation Date: Apr 30, 2023 at 5:36:57 PM
 *********************************************/



// int unique_values = 5;
// range range_unique_values = 1..unique_values;

// int size_of_board = 5;
// range range_size = 1..size_of_board;

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

// int board_state[range_unique_values][range_size][range_size] = 
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
range range_size = 1..size_of_board;

int search_depth = size_of_board - 1;
range range_search_depth = 1..search_depth;


int board_state[range_unique_values][range_size][range_size] = 
[[[0, 1], [0, 0]], [[1, 0], [1, 1]]];



// decision 0 - white, 1 - black
dvar boolean decision[range_size][range_size];

dexpr float total_coverage = sum(i in range_size) sum(j in range_size) decision[i][j];

maximize total_coverage;

subject to {
    Repeating_Numbers_in_Rows:
    forall(r in range_unique_values) {
        forall(x in range_size) {
            sum(i in range_size) decision[x][i]*board_state[r][x][i] <= 1;
        }
    }

    Repeating_Numbers_in_Columns:
    forall(r in range_unique_values) {
        forall(y in range_size) {
            sum(i in range_size) decision[i][y]*board_state[r][i][y] <= 1;
        }
    }
    
    Adjacent_Black_by_Row:
    forall(r in range_size) {
        forall(y in range_search_depth) {
            decision[r][y] + decision[r][y+1] <= 1;
        }
    }

    Adjacent_Black_by_Column:
    forall(c in range_size) {
        forall(x in range_search_depth) {
            decision[x][c] + decision[x+1][c] <= 1;
        }
    }
    // TODO: Add third constraint
}
