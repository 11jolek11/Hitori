import numpy as np


def convert(board:np.ndarray):
    unique_numbers = np.unique(board)
    result = np.zeros([len(unique_numbers), *board.shape])
    for number in range(result.shape[0]):
        for y in range(board.shape[0]):
            for x in range(board.shape[1]):
                if board[y][x] == unique_numbers[number]:
                    result[number][y][x] = 1
    result = result.astype(int)
    return result.tolist()


def writer(board:np.ndarray, dat_file: str="./task.dat"):
    size_of_board = len(board)
    unique_values = len(np.unique(board))
    converted_board = convert(board)
    content = f"""
    unique_values = {unique_values};
    size_of_board = {size_of_board};
    board_state = {converted_board};
    """
    print(content)
    with open(dat_file, "w") as file:
        file.write(content)

if __name__ == "__main__":
    from problems import *
    writer(np.asarray(HITORI_PROBLEM_1))
