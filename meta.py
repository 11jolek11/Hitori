# import random

# # Function to calculate the score of the current state
# def calculate_score(matrix):
#     score = 0
#     n = len(matrix)

#     # Check rows for duplicates
#     for i in range(n):
#         row = set()
#         for j in range(n):
#             if matrix[i][j] in row:
#                 score += 1
#             else:
#                 row.add(matrix[i][j])

#     # Check columns for duplicates
#     for j in range(n):
#         column = set()
#         for i in range(n):
#             if matrix[i][j] in column:
#                 score += 1
#             else:
#                 column.add(matrix[i][j])

#     return score


# # Function to get neighbors of a given state
# def get_neighbors(matrix):
#     neighbors = []

#     n = len(matrix)

#     for i in range(n):
#         for j in range(n):
#             neighbor = [row[:] for row in matrix]  # Create a copy of the matrix

#             # Flip the value (0 -> 1 or 1 -> 0) at position (i, j)
#             neighbor[i][j] = 1 - neighbor[i][j]

#             neighbors.append(neighbor)

#     return neighbors


# # Function to apply Tabu Search to solve Hitori puzzles
# def solve_hitori_puzzle(puzzle):
#     n = len(puzzle)
#     tabu_list = []
#     current_state = puzzle

#     # Set the maximum number of iterations and the tabu list size
#     max_iterations = 100
#     tabu_list_size = 10

#     for iteration in range(max_iterations):
#         current_score = calculate_score(current_state)

#         if current_score == 0:  # Puzzle solved
#             return current_state

#         neighbors = get_neighbors(current_state)

#         best_neighbor = None
#         best_neighbor_score = float('inf')

#         for neighbor in neighbors:
#             if neighbor not in tabu_list:
#                 neighbor_score = calculate_score(neighbor)

#                 if neighbor_score < best_neighbor_score:
#                     best_neighbor = neighbor
#                     best_neighbor_score = neighbor_score

#         if best_neighbor is None:  # No non-tabu neighbors found
#             return current_state

#         tabu_list.append(best_neighbor)

#         if len(tabu_list) > tabu_list_size:
#             tabu_list.pop(0)  # Remove the oldest entry from the tabu list

#         current_state = best_neighbor

#     return current_state


# # Example usage
# puzzle = [
#     [1, 2, 2, 4],
#     [1, 1, 3, 4],
#     [3, 2, 1, 3],
#     [4, 3, 4, 2]
# ]

# solution = solve_hitori_puzzle(puzzle)

# # Printing the solution
# for row in solution:
#     print(row)

# ###################################################################################################################
# ###################################################################################################################
# ###################################################################################################################
# ###################################################################################################################
# ###################################################################################################################


# import random
# import numpy as np

# # Define the Hitori puzzle board
# # The board is represented as a 2D array, where 0 represents an empty cell and any positive number represents a shaded cell
# # For example, board[row][col] = 1 represents a shaded cell at position (row, col)

# # Define the size of the puzzle board
# BOARD_SIZE = 5

# # Define the initial state of the puzzle board
# initial_board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# # Define the Tabu Search parameters
# MAX_ITERATIONS = 100000
# TABU_TENURE = 100

# # Define the Hitori puzzle instance
# # The puzzle instance is represented as a 2D array, where each element represents the value of a cell in the puzzle
# puzzle_instance = np.array([[2, 2, 3, 1, 4],
#                             [5, 5, 3, 3, 1],
#                             [5, 4, 2, 3, 1],
#                             [1, 5, 4, 2, 3],
#                             [1, 1, 1, 4, 4]])







# # Function to calculate the fitness score of a solution
# def calculate_fitness(solution):
#     """
#     Calculate the fitness score of a solution.

#     Parameters:
#     - solution: 2D array representing the solution (puzzle board)

#     Returns:
#     - fitness_score: Fitness score of the solution
#     """
#     # Initialize a set to store visited numbers
#     visited_numbers = set()

#     # Calculate the fitness score by counting the number of unique numbers in each row and column
#     fitness_score = 0
#     for row in range(BOARD_SIZE):
#         visited_numbers.clear()
#         for col in range(BOARD_SIZE):
#             cell_value = solution[row][col]
#             if cell_value == 0 or cell_value in visited_numbers:
#                 fitness_score += 1
#             visited_numbers.add(cell_value)

#     for col in range(BOARD_SIZE):
#         visited_numbers.clear()
#         for row in range(BOARD_SIZE):
#             cell_value = solution[row][col]
#             if cell_value == 0 or cell_value in visited_numbers:
#                 fitness_score += 1
#             visited_numbers.add(cell_value)
#     print(fitness_score)
#     return fitness_score

# # Function to generate the initial solution
# def generate_initial_solution():
#     """
#     Generate the initial solution.

#     Returns:
#     - solution: 2D array representing the initial solution (puzzle board)
#     """
#     # Create a copy of the initial board
#     solution = np.copy(initial_board)

#     # Randomly shade cells in the solution based on the puzzle instance
#     for row in range(BOARD_SIZE):
#         for col in range(BOARD_SIZE):
#             if random.random() < 0.5:
#                 solution[row][col] = puzzle_instance[row][col]

#     return solution

# # Function to generate neighboring solutions
# def generate_neighbors(solution):
#     """
#     Generate neighboring solutions for a given solution.

#     Parameters:
#     - solution: 2D array representing the current solution (puzzle board)

#     Returns:
#     - neighbors: List of neighboring solutions
#     """
#     neighbors = []

#     # Iterate over each cell in the solution


#     for row in range(BOARD_SIZE):
#         for col in range(BOARD_SIZE):
#             # Create a copy of the current solution
#             neighbor = np.copy(solution)

#             # Toggle the shading of the current cell
#             neighbor[row][col] = 0 if neighbor[row][col] > 0 else puzzle_instance[row][col]

#             # Add the neighbor to the list
#             neighbors.append(neighbor)

#     return neighbors

# # Function to apply Tabu Search to solve the Hitori puzzle
# def tabu_search():
#     """
#     Apply Tabu Search to solve the Hitori puzzle.

#     Returns:
#     - best_solution: 2D array representing the best solution found
#     """
#     # Generate the initial solution
#     current_solution = generate_initial_solution()
#     best_solution = np.copy(current_solution)
#     best_fitness = calculate_fitness(best_solution)

#     # Initialize the Tabu list
#     tabu_list = []

#     # Start the Tabu Search iterations
#     iterations = 0
#     while iterations < MAX_ITERATIONS:
#         # Generate neighboring solutions
#         neighbors = generate_neighbors(current_solution)

#         # Select the best neighbor that is not in the Tabu list
#         best_neighbor = None
#         best_neighbor_fitness = float('inf')

#         for neighbor in neighbors:
#             neighbor_fitness = calculate_fitness(neighbor)

#             if neighbor_fitness < best_neighbor_fitness and neighbor.tolist() not in tabu_list:
#                 best_neighbor = neighbor
#                 best_neighbor_fitness = neighbor_fitness

#         # Update the current solution and best solution
#         current_solution = best_neighbor

#         if best_neighbor_fitness < best_fitness:
#             best_solution = np.copy(best_neighbor)
#             best_fitness = best_neighbor_fitness

#         # Add the current solution to the Tabu list
#         tabu_list.append(current_solution.tolist())

#         # Remove the oldest solution from the Tabu list if it exceeds the Tabu tenure
#         if len(tabu_list) > TABU_TENURE:
#             tabu_list.pop(0)

#         # Increment the iterations counter
#         iterations += 1

#     return best_solution

# # Solve the Hitori puzzle using Tabu Search
# solution = tabu_search()

# # Print the solution
# print("Solution:")
# print(solution)



# ###################################################################################################################
# ###################################################################################################################
# ###################################################################################################################
# ###################################################################################################################
# ###################################################################################################################


import random
import numpy as np

# Define the Hitori puzzle board
# The board is represented as a 2D array, where 0 represents an empty cell and any positive number represents a shaded cell
# For example, board[row][col] = 1 represents a shaded cell at position (row, col)

# Define the size of the puzzle board
BOARD_SIZE = 5

# Define the initial state of the puzzle board
initial_board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# Define the Tabu Search parameters
MAX_ITERATIONS = 10000
TABU_TENURE = 100

# Define the Hitori puzzle instance
# The puzzle instance is represented as a 2D array, where each element represents the value of a cell in the puzzle
puzzle_instance = np.array([[2, 2, 3, 1, 4],
                            [5, 5, 3, 3, 1],
                            [5, 4, 2, 3, 1],
                            [1, 5, 4, 2, 3],
                            [1, 1, 1, 4, 4]])


def count_repeating_numbers(matrix, target):
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


# Function to calculate the fitness score of a solution
def calculate_fitness(solution):
    # TODO: add penalty for repeating numbers (non-zero numbers)
    # TODO: add penalty for adjacent black cells
    # TODO: add penalty for closed structures
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

    return fitness_score

# Function to generate the initial solution
def generate_initial_solution():
    """
    Generate the initial solution.

    Returns:
    - solution: 2D array representing the initial solution (puzzle board)
    """
    # Create a copy of the initial board
    solution = np.copy(initial_board)

    # Randomly shade cells in the solution based on the puzzle instance
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if random.random() < 0.5:
                solution[row][col] = puzzle_instance[row][col]

    return solution


def generate_neighbors(solution):
    # TODO: Find better solution
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

    # Start the Tabu Search iterations
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

        # Remove the oldest solution from the Tabu list if it exceeds the Tabu tenure
        if len(tabu_list) > TABU_TENURE:
            tabu_list.pop(0)

        # Increment the iterations counter
        iterations += 1

    return best_solution


solution = tabu_search()

# Print the solution
print("Solution:")
print(solution)
