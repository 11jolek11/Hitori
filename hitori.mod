/*********************************************
 * OPL 22.1.1 Model
 * Author: Andrzej Dabrowski
 * Creation Date: Apr 30, 2023 at 5:36:57 PM
 *********************************************/


// int size_of_board = 8;

// range range_size = 1..size_of_board;

// int board_state[range_size][range_size] = [
//     [4, 8, 1,6, 3, 2, 5, 7],
//     [3, 6, 7, 2, 1, 6, 5, 4],
//     [2, 3, 4, 8, 2, 8, 6, 1],
//     [4, 1, 6, 5, 7, 7, 3, 5],
//     [7, 2, 3, 1, 8, 5, 1, 2],
//     [3, 5, 6, 7, 3, 1, 8, 4],
//     [6, 4, 2, 3, 5, 4, 7, 8],
//     [8, 7, 1, 4, 2, 3, 5, 6],
// ];

int unique_values;

int size_of_board = 5;

range range_size = 1..size_of_board;


int search_depth = size_of_board - 1;

range range_search_depth = 1..search_depth;

// int board_state[range_size][range_size] = [
//     [2, 3, 2, 1, 5],
//     [2, 4, 1, 3, 5],
//     [2, 1, 2, 2, 5],
//     [1, 5, 2, 4, 3],
//     [2, 2, 5, 5, 2]];

int board_state[unique_values][range_size][range_size] = 
[
    [
        [0, 0, 0, 1, 0], 
        [0, 0, 1, 0, 0], 
        [0, 1, 0, 0, 0], 
        [1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0]
        ], 
    [
        [1, 0, 1, 0, 0], 
        [1, 0, 0, 0, 0], 
        [1, 0, 1, 1, 0], 
        [0, 0, 1, 0, 0], 
        [1, 1, 0, 0, 1]
        ], 
    [
        [0, 1, 0, 0, 0], 
        [0, 0, 0, 1, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0]
        ],
    [
        [0, 0, 0, 0, 0], 
        [0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0], 
        [0, 0, 0, 0, 0]
        ], 
    [
        [0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 1], 
        [0, 1, 0, 0, 0], 
        [0, 0, 1, 1, 0]
        ]
];

// decision 0 - white, 1 - black
dvar boolean decision[range_size][range_size];

dexpr float total_coverage = sum(i in range_size) sum(j in range_size) decision[i][j];

maximize total_coverage;

subject to {
    Repeating_Numbers_in_Rows:
    forall(r in range_size) {
        forall(x in range_size) {
            forall(y in range_size) {
                if (board_state[x][r] == board_state[y][r] ) {
                    decision[r][x] + decision[r][y] > 0;
                }
            }
        }
    }

    Repeating_Numbers_in_Columns:
    forall(c in range_size) {
        forall(x in range_size) {
            forall(y in range_size) {
                if (board_state[c][x] == board_state[c][y] ) {
                    decision[c][x] + decision[c][y] > 0;
                }
            }
        }
    }

    Adjacent_Black_by_Row:
    forall(r in range_size) {
        forall(y in search_depth) {
            if (board_state[y][r] == board_state[y+1][r] ) {
                decision[r][y] + decision[r][y+1] <= 2;
            }
        }
    }

    Adjacent_Black_by_Column:
    forall(c in range_size) {
        forall(x in search_depth) {
                if (board_state[c][x] == board_state[c][y] ) {
                    decision[c][x] + decision[c][y] <= 2;
            }
        }
    }
    // TODO: Add third constraint
}
