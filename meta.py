import random
import numpy as np
from problems import *


# Define the Hitori puzzle board

# Define the size of the puzzle board
BOARD_SIZE = 5

initial_board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# Define the parameters
MAX_ITERATIONS = 1000
TABU_MAX = 10

# puzzle_instance = np.array([[2, 2, 3, 1, 4],
#                             [5, 5, 3, 3, 1],
#                             [5, 4, 2, 3, 1],
#                             [1, 5, 4, 2, 3],
#                             [1, 1, 1, 4, 4]])


# puzzle_instance = np.array(
#                     [[2, 2, 1, 5, 3],
#                      [2, 3, 1, 4, 5],
#                      [1, 1, 1, 3, 5],
#                      [1, 3, 5, 4, 2],
#                      [5, 4, 3, 2, 1]]
#                    )
puzzle_instance = np.array(HITORI_PROBLEM_1)


def count_repeating_numbers(matrix, target):
    """
    Count repeating number (target) in columns and rows

    Parameters:
    - matrix: 2D array representing the solution (puzzle board)
    - target: symbol/number function is counting

    Returns:
    - count: Number of repeating numbers found
    """
    count = 0

    # Check horizontally
    for row in matrix:
        consecutive_count = 0
        for num in row:
            if num == target:
                consecutive_count += 1
                count += 1 if consecutive_count == 2 else 0
            else:
                consecutive_count = 0

    # Check vertically
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for col in range(num_cols):
        consecutive_count = 0
        for row in range(num_rows):
            if matrix[row][col] == target:
                consecutive_count += 1
                count += 1 if consecutive_count == 2 else 0
            else:
                consecutive_count = 0
    return count

def count_adjacent_black(matrix, symbol=0):
    """
    Count shaded cells, which are next to each other in columns and rows

    Parameters:
    - matrix: 2D array representing the solution (puzzle board)
    - symbol: symbol/number representing shaded cell

    Returns:
    - count: Number of shaded cells which are next to each other
    """
    count = 0
    for cell_x in range(len(matrix)):
        for cell_y in range(len(matrix)-1):
            count += 1 if matrix[cell_y][cell_x] == 0 and matrix[cell_y+1][cell_x] == 0 else 0
    for cell_y in range(len(matrix)):
        for cell_x in range(len(matrix)-1):
            count += 1 if matrix[cell_y][cell_x] == 0 and matrix[cell_y][cell_x+1] == 0 else 0
    return count

def detect_closed_shape(matrix, symbol=0):
    temp = matrix
    matrix = np.zeros((3*BOARD_SIZE, 3*BOARD_SIZE))
    nb = matrix.shape[0]
    na = temp.shape[0]
    lower = (nb) // 2 - (na // 2) - 1
    upper = (nb // 2) + (na // 2)
    # print(upper)
    # print(lower)
    matrix[lower:upper, lower:upper] = temp
    for n in range(BOARD_SIZE-1):
        total = 0
        for y in range(BOARD_SIZE, 2*BOARD_SIZE):
            for x in range(BOARD_SIZE, 2*BOARD_SIZE):
                for p in range(n):
                    if matrix[y-1+p][x+1+n-p] + matrix[y-1+p][x-1-n+p] + matrix[y+1-p][x+1+n-p] + matrix[y+1-p][x-1-n+p] == 0:
                        total += 4 
        if total > 4*n + 4 -1:
            return 10
    return 0

# Function to calculate the fitness score of a solution
def calculate_fitness(solution):
    """
    Calculate the fitness score of a solution.

    Parameters:
    - solution: 2D array representing the solution (puzzle board)

    Returns:
    - fitness_score: Fitness score of the solution
    """
    # Initialize a set to store visited numbers
    visited_numbers = set()

    # Calculate the fitness score by counting the number of unique numbers in each row and column
    fitness_score = 0
    for row in range(BOARD_SIZE):
        visited_numbers.clear()
        for col in range(BOARD_SIZE):
            cell_value = solution[row][col]
            if cell_value == 0 or cell_value in visited_numbers:
                fitness_score += 1
            visited_numbers.add(cell_value)

    for col in range(BOARD_SIZE):
        visited_numbers.clear()
        for row in range(BOARD_SIZE):
            cell_value = solution[row][col]
            if cell_value == 0 or cell_value in visited_numbers:
                fitness_score += 1
            visited_numbers.add(cell_value)

    fitness_score += 20*count_adjacent_black(solution)

    fitness_score += detect_closed_shape(solution)

    return fitness_score

# Function to generate the initial solution
def generate_initial_solution():
    """
    Generate the initial solution.

    Returns:
    - solution: 2D array representing the initial solution (puzzle board)
    """
    solution = np.copy(initial_board)

    # Randomly shade cells in the solution based on the puzzle instance
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if random.random() < 0.5:
                solution[row][col] = puzzle_instance[row][col]

    return solution


def generate_neighbors(solution):
    neighbors = []

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            neighbor = np.copy(solution)

            # Toggle the shading of the current cell
            neighbor[row][col] = 0 if neighbor[row][col] > 0 else puzzle_instance[row][col]

            neighbors.append(neighbor)

    return neighbors


def tabu_search():
    # Generate the initial solution
    current_solution = generate_initial_solution()
    best_solution = np.copy(current_solution)
    best_fitness = calculate_fitness(best_solution)

    tabu_list = []

    # Start the tabu search
    iterations = 0
    while iterations < MAX_ITERATIONS:
        # Generate neighboring solutions
        neighbors = generate_neighbors(current_solution)

        # Select the best neighbor that is not in the Tabu list
        best_neighbor = None
        best_neighbor_fitness = float('inf')

        for neighbor in neighbors:
            neighbor_fitness = calculate_fitness(neighbor)

            if neighbor_fitness < best_neighbor_fitness and neighbor.tolist() not in tabu_list:
                best_neighbor = neighbor
                best_neighbor_fitness = neighbor_fitness

        # Check if a better solution is found in the Tabu list
        if best_neighbor is None:
            for tabu_solution in tabu_list:
                tabu_fitness = calculate_fitness(tabu_solution)

                if tabu_fitness < best_neighbor_fitness:
                    best_neighbor = np.copy(tabu_solution)
                    best_neighbor_fitness = tabu_fitness

                    # Remove the solution from the Tabu list
                    tabu_list.remove(tabu_solution)

        # Update the current solution and best solution
        current_solution = best_neighbor

        if best_neighbor_fitness < best_fitness:
            best_solution = np.copy(best_neighbor)
            best_fitness = best_neighbor_fitness

        # Add the current solution to the Tabu list
        tabu_list.append(current_solution.tolist())

        # Remove the oldest solution from the Tabu
        if len(tabu_list) > TABU_MAX:
            tabu_list.pop(0)

        iterations += 1

    return best_solution


def display(board:np.ndarray):
    for y in range(board.shape[0]):
        row = ""
        for x in range(board.shape[0]):
            value = "█" if board[y][x] == 0 else str(board[y][x])
            row += f"{value} "
        print(row)



if __name__ == "__main__":
    solution = tabu_search()

    # Print the solution
    print("Solution:")
    display(solution)
