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
    print(result.dtype)
    return result.tolist()
    # return result


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
    HITORI_PROBLEM_1 = np.asarray(( 
                     (2, 2, 1, 5, 3),
                     (2, 3, 1, 4, 5),
                     (1, 1, 1, 3, 5),
                     (1, 3, 5, 4, 2),
                     (5, 4, 3, 2, 1),
                   ))
    print(len(convert(HITORI_PROBLEM_1)))
    print(convert(HITORI_PROBLEM_1))

