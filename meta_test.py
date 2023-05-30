# import random


# def initialize_solution(board):
#     """Initialize the solution by randomly shading some cells."""
#     size = len(board)
#     solution = [[0 for _ in range(size)] for _ in range(size)]
#     for i in range(size):
#         for j in range(size):
#             if random.random() < 0.5:
#                 solution[i][j] = board[i][j]
#     return solution


# def calculate_score(solution):
#     """Calculate the score of the solution."""
#     score = 0
#     size = len(solution)
#     for i in range(size):
#         for j in range(size):
#             if solution[i][j] != 0:
#                 score += 1
#     return score


# def get_neighboring_solutions(solution):
#     """Generate neighboring solutions by flipping shaded and unshaded cells."""
#     size = len(solution)
#     neighbors = []
#     for i in range(size):
#         for j in range(size):
#             neighbor = [row[:] for row in solution]
#             neighbor[i][j] = 0 if neighbor[i][j] != 0 else -1
#             neighbors.append(neighbor)
#     return neighbors


# def apply_tabu_search(board, max_iterations, max_tabu_length):
#     """Apply the Tabu Search algorithm to solve the Hitori puzzle."""
#     size = len(board)
#     best_solution = initialize_solution(board)
#     best_score = calculate_score(best_solution)
#     tabu_list = []
#     iteration = 0

#     while iteration < max_iterations:
#         neighbors = get_neighboring_solutions(best_solution)
#         best_neighbor = None
#         best_neighbor_score = float('-inf')

#         for neighbor in neighbors:
#             if neighbor in tabu_list:
#                 continue

#             neighbor_score = calculate_score(neighbor)
#             if neighbor_score > best_neighbor_score:
#                 best_neighbor = neighbor
#                 best_neighbor_score = neighbor_score

#         if best_neighbor is None:
#             break

#         best_solution = best_neighbor
#         best_score = best_neighbor_score

#         tabu_list.append(best_solution)
#         if len(tabu_list) > max_tabu_length:
#             tabu_list.pop(0)

#         iteration += 1

#     return best_solution


# # Example usage
# puzzle = [
#     [4, 5, 1, 3],
#     [2, 1, 4, 3],
#     [3, 4, 2, 1],
#     [1, 3, 3, 2]
# ]

# solution = apply_tabu_search(puzzle, max_iterations=10000, max_tabu_length=100)
# for row in solution:
#     print(row)
