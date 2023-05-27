import numpy as np


# orginal size 7x7
# table=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]]
# table=[[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21]]

# table=[[0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]]
cover = np.asarray(
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0   1  0
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 1   2  1
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 2   3  2
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 3   4  3
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 4   5  4
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 5   6  5
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 6   7  6
# -----------------------------$-----------------$--------------------------------
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 0   8  7
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 1   9  8 
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 2   10 9
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 3   11 10
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 4   12 11
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 5   13 12
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 6   14 13
# -----------------------------$-----------------$--------------------------------
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0   15 14
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 1   16 15
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 2   17 16
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 3   18 17
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 4   19 18
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 5   20 19
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # 6   21 20
)

# orginal size 7x7
# table=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]]
# table=[[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21]]

# table=[[0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]]
table = np.asarray(
        [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0   1  0
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 1   2  1
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 2   3  2
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 3   4  3
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 4   5  4
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 5   6  5
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 6   7  6
# -----------------------------$-----------------$--------------------------------
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 0   8  7
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 1   9  8 
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 2   10 9
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 3   11 10
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 4   12 11
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 5   13 12
         [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 6   14 13
# -----------------------------$-----------------$--------------------------------
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0   15 14
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 1   16 15
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 2   17 16
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 3   18 17
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 4   19 18
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 5   20 19
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # 6   21 20
)


def check(element: list):
  if sum(element) == len(element):
    raise ValueError("Detected 1")


size = 7
for n in range(1, 7):
# for n in range(1, 2):
  for x_i in range(size, 2*size):
    for y_i in range(size, 2*size):
  # for x_i in range(0, 1*size):
  #   for y_i in range(0, 1*size):
      extra_x, extra_y = x_i-n, y_i-n
      # n = 3
      temp = []
      tracker = []
      for i in range(n+1):
        cover[x_i][y_i] = 9
        temp.append(table[extra_x + i][extra_y + n-i])
        tracker.append((extra_x + i, extra_y + n-i))
        cover[extra_x + i][extra_y + n-i] = 2
        # print(([extra_x + i+n],[extra_y + 2*n-i]))
        temp.append(table[extra_x + i+n][extra_y + 2*n-i])
        tracker.append((extra_x + i+n, extra_y + 2*n-i))
        cover[extra_x + i+n][extra_y + 2*n-i] = 2

        temp.append(table[extra_x + i][extra_y + i+n])
        tracker.append((extra_x + i, extra_y + n+i))
        cover[extra_x + i][extra_y + i+n] = 2

        temp.append(table[extra_x + i+n][extra_y + i])
        tracker.append((extra_x + i + n, extra_y + i))
        cover[extra_x + i+n][extra_y + i] = 2

        # cover[extra_x + i][extra_y + n-i] = 1
        # cover[extra_x + i+n][extra_y + 2*n-i] = 1
        # cover[extra_x + i][extra_y + i+n] = 1
        # cover[extra_x + i+n][extra_y + i] = 1

        # cover[extra_x][extra_y] = 9
        # cover[extra_x][extra_y] = 9
        # cover[extra_x][extra_y] = 9
        # cover[extra_x][extra_y] = 9
      # print(tracker)
      check(temp)


# size = 7
# for n in range(1, 6):
# # for n in range(1, 2):
#   for x_i in range(size, 2*size):
#     for y_i in range(size, 2*size):
#   # for x_i in range(0, 1*size):
#   #   for y_i in range(0, 1*size):
#       extra_x, extra_y = x_i-n, y_i-n
#       # n = 3
#       temp = []
#       counter = 0
#       tracker = []
#       for i in range(n+1):
#         temp.append(table[extra_x + i][extra_y + n-i])
#         counter += table[extra_x + i][extra_y + n-i] + table[extra_x + i+n][extra_y + 2*n-i] + table[extra_x + i][extra_y + i+n] + table[extra_x + i+n][extra_y + i]
#         tracker.append((extra_x + i, extra_y + n-i))
#         # print(([extra_x + i+n],[extra_y + 2*n-i]))
#         temp.append(table[extra_x + i+n][extra_y + 2*n-i])
#         tracker.append((extra_x + i+n, extra_y + 2*n-i))

#         temp.append(table[extra_x + i][extra_y + i+n])
#         tracker.append((extra_x + i, extra_y + n+i))

#         temp.append(table[extra_x + i+n][extra_y + i])
#         tracker.append((extra_x + i + n, extra_y + i))
#       # print(counter)
#       # poniewz przejdzie dwa razy
#       if counter >= n*8:
#         print(tracker)
#         raise ValueError("Detected 1")


size = 7
for n in range(1, 7):
  for x_i in range(size, 2*size):
    for y_i in range(size, 2*size):
      for x in range()
      # extra_x, extra_y = x_i-n, y_i-n
      # temp = []
      # tracker = []
      # for i in range(n+1):
      #   cover[x_i][y_i] = 9
      #   temp.append(table[extra_x + i][extra_y + n-i])
      #   tracker.append((extra_x + i, extra_y + n-i))
      #   cover[extra_x + i][extra_y + n-i] = 2
      #   # print(([extra_x + i+n],[extra_y + 2*n-i]))
      #   temp.append(table[extra_x + i+n][extra_y + 2*n-i])
      #   tracker.append((extra_x + i+n, extra_y + 2*n-i))
      #   cover[extra_x + i+n][extra_y + 2*n-i] = 2

      #   temp.append(table[extra_x + i][extra_y + i+n])
      #   tracker.append((extra_x + i, extra_y + n+i))
      #   cover[extra_x + i][extra_y + i+n] = 2

      #   temp.append(table[extra_x + i+n][extra_y + i])
      #   tracker.append((extra_x + i + n, extra_y + i))
      #   cover[extra_x + i+n][extra_y + i] = 2
      # check(temp)




