import numpy as np



def convert(board:np.ndarray):
    unique_numbers = np.unique(board)
    result = np.zeros([len(unique_numbers), *board.shape])
    for number in range(result.shape[0]):
        for y in range(board.shape[0]):
            for x in range(board.shape[1]):
                if board[y][x] == unique_numbers[number]:
                    result[number][y][x] = 1
    # print("######################################")
    # # print(result)
    # print("######################################")
    result = result.astype(int)
    # print(result.dtype)
    return result.tolist()
    # return result

def writer(board:np.ndarray, dat_file: str="./task.dat"):
    header = r"""
    
    """
    size_of_board = len(board)
    unique_values = len(np.unique(board))
    converted_board = convert(board)
    with open(dat_file, "w"):
        pass

    

if __name__ == "__main__":
    # test = np.array([[2, 2], [2, 3]])
    # test = np.array(
    #     [
    #         [2, 3, 2, 1, 5],
    #         [2, 4, 1, 3, 5],
    #         [2, 1, 2, 2, 5],
    #         [1, 5, 2, 4, 3],
    #         [2, 2, 5, 5, 2]
    #     ]
    # )
    # test = np.array(
    #         [
    #             [2, 1],
    #             [2, 2]
    #         ]
    #     )
    # print(convert(test))

    #-----------------------------------------------------------------------------
    # Initialize the problem data
    #-----------------------------------------------------------------------------

    # Problem 0 (for test). A solution is:
    #   * 2 *
    #   2 3 1
    #   * 1 *
    HITORI_PROBLEM_0 = ( (2, 2, 1),
                        (2, 3, 1),
                        (1, 1, 1),
                    )

    #   * 2 * 5 3
    #   2 3 1 4 *
    #   * 1 * 3 5
    #   1 * 5 * 2
    #   5 4 3 2 1
    HITORI_PROBLEM_1 = ( (2, 2, 1, 5, 3),
                        (2, 3, 1, 4, 5),
                        (1, 1, 1, 3, 5),
                        (1, 3, 5, 4, 2),
                        (5, 4, 3, 2, 1),
                    )
    # Problem 2. A solution is:
    #   * 8 * 6 3 2 * 7
    #   3 6 7 2 1 * 5 4
    #   * 3 4 * 2 8 6 1
    #   4 1 * 5 7 * 3 *
    #   7 * 3 * 8 5 1 2
    #   * 5 6 7 * 1 8 *
    #   6 * 2 3 5 4 7 8
    #   8 7 1 4 * 3 * 6
    HITORI_PROBLEM_2 = ( (4, 8, 1, 6, 3, 2, 5, 7),
                        (3, 6, 7, 2, 1, 6, 5, 4),
                        (2, 3, 4, 8, 2, 8, 6, 1),
                        (4, 1, 6, 5, 7, 7, 3, 5),
                        (7, 2, 3, 1, 8, 5, 1, 2),
                        (3, 5, 6, 7, 3, 1, 8, 4),
                        (6, 4, 2, 3, 5, 4, 7, 8),
                        (8, 7, 1, 4, 2, 3, 5, 6),
                    )

    # Problem 3, solution to discover !
    HITORI_PROBLEM_3 = ( ( 2,  5,  6,  3,  8, 10,  7,  4, 13,  6, 14, 15,  9,  4,  1),
                        ( 3,  1,  7, 12,  8,  4, 10,  4,  4, 11,  5, 13,  4,  9,  2),
                        ( 4, 14, 10, 10, 14,  5, 11,  1,  6,  2,  7, 11, 13, 15, 12),
                        ( 5, 10,  2,  5, 13,  3,  8,  5,  9,  7,  4, 10,  6, 10,  2),
                        ( 1,  6,  8, 15, 10,  7,  4,  2, 15, 14,  9,  3,  3, 11,  4),
                        ( 6, 14,  3, 11,  2,  4,  9,  5,  7, 13, 12,  8, 10, 14,  1),
                        (12,  8, 14, 11,  3,  7, 15, 13, 10,  7, 12, 13,  5,  2, 13),
                        (11,  4, 12, 15,  5,  6,  5,  3, 15, 10,  7,  9,  5, 13, 14),
                        ( 8, 15,  4,  6, 15,  3, 13, 14,  6, 12, 10,  1, 11,  3,  5),
                        (15, 15,  9, 12,  1,  8, 11, 10,  2,  2, 11,  9,  4, 12,  2),
                        ( 7,  1,  9,  9, 10,  5,  3, 11, 13,  6,  7,  4, 12,  5,  8),
                        (14, 10, 13,  4, 12, 15, 11, 10,  5,  7,  8, 12,  5,  3,  6),
                        ( 5, 10, 11,  5, 11, 14, 14, 15,  8, 13, 13,  2,  7,  9,  9),
                        ( 9,  7, 15, 10, 12, 11,  8,  6,  1,  5,  7, 14, 13,  1,  3),
                        ( 6,  9,  1, 13,  6,  4, 12,  7, 14,  4,  2,  1,  3,  8, 12)
                    )


    # print(len(convert(HITORI_PROBLEM_1)))
    print(convert(np.asarray(HITORI_PROBLEM_1)))
    # writer(np.asarray(HITORI_PROBLEM_1))

