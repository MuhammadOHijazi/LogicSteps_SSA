from queue import Queue


class Levels:
    # create all the levels by objects
    levels = Queue(maxsize=100)

    def __init__(self, num_rows, num_columns, grid_level, player_positions):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.grid_level = grid_level
        self.player_positions = player_positions

    start_cost = 1
    # creating level1
    # player in the 0
    level1_grid = [[0, 1, 1, 1]]
    num_rows_1 = 1
    num_columns_1 = 4
    level1_psp = [(0, 0)]
    to_win_1 = 3
    level1 = [num_rows_1, num_columns_1, level1_grid, level1_psp, to_win_1, start_cost]
    levels.put(level1)

    # creating level 2
    level2_grid = [[1, 2, 2, 2, 1]]
    num_rows_2 = 1
    num_columns_2 = 5
    level2_psp = [(0, 0)]
    to_win_2 = 8
    level2 = [num_rows_2, num_columns_2, level2_grid, level2_psp, to_win_2, start_cost]
    levels.put(level2)

    # creating level 3
    level3_grid = [[-1, 1, 1],
                   [0, 2, 1],
                   [-1, 1, -1]]
    num_rows_3 = len(level3_grid)
    num_columns_3 = len(level3_grid[0])
    level3_psp = [(1, 0)]
    to_win_3 = 6
    level3 = [num_rows_3, num_columns_3, level3_grid, level3_psp, to_win_3, start_cost]
    levels.put(level3)

    # creating level 4
    # Two player on the 0 values
    level4_grid = [[-1, -1, 1, -1, -1],
                   [-1, -1, 1, -1, -1],
                   [0, 1, 2, 1, 1],
                   [-1, -1, 1, -1, -1],
                   [-1, -1, 0, -1, -1]]
    num_rows_4 = len(level4_grid)
    num_columns_4 = len(level4_grid[0])
    level4_psp = [(2, 0), (4, 2)]
    to_win_4 = 8
    level4 = [num_rows_4, num_columns_4, level4_grid, level4_psp, to_win_4, start_cost, start_cost]
    levels.put(level4)

    # creating level 5
    level5_grid = [[-1, 2, 2, 2, 1],
                   [-1, 2, 2, 2, 1]]
    num_rows_5 = len(level5_grid)
    num_columns_5 = len(level5_grid[0])
    level5_psp = [(0, 0)]
    to_win_5 = 14
    level5 = [num_rows_5, num_columns_5, level5_grid, level5_psp, to_win_5, start_cost]
    levels.put(level5)

    # creating level 6
    level6_grid = [[1, 2, 1],
                   [1, 2, 1],
                   [1, 2, 1],
                   [-1, 0, -1]]
    num_rows_6 = len(level6_grid)
    num_columns_6 = len(level6_grid[0])
    level6_psp = [(3, 1)]
    to_win_6 = 12
    level6 = [num_rows_6, num_columns_6, level6_grid, level6_psp, to_win_6, start_cost]
    levels.put(level6)

    # creating level 7
    level7_grid = [[-1, 1, 3, 2, -1],
                   [-1, -1, -1, 1, -1],
                   [0, 1, 2, 3, 1]]
    num_rows_7 = len(level7_grid)
    num_columns_7 = len(level7_grid[0])
    level7_psp = [(2, 0)]
    to_win_7 = 14
    level7 = [num_rows_7, num_columns_7, level7_grid, level7_psp, to_win_7, start_cost]
    levels.put(level7)

    # creating level 8
    level8_grid = [[-1, -1, 2, 2, 1],
                   [1, -1, 1, -1, 1],
                   [2, 1, 2, 2, 1]]
    num_rows_8 = len(level8_grid)
    num_columns_8 = len(level8_grid[0])
    level8_psp = [(2, 1)]
    to_win_8 = 16
    level8 = [num_rows_8, num_columns_8, level8_grid, level8_psp, to_win_8, start_cost]
    levels.put(level8)

    # creating level 9
    # two player in the game (the first is on the (1,1) and the second in (2,2))
    level9_grid = [[-1, -1, 1],
                   [1, 1, 2],
                   [-1, 2, 2]]
    num_rows_9 = len(level9_grid)
    num_columns_9 = len(level9_grid[0])
    level9_psp = [(1, 1), (2, 2)]
    to_win_9 = 9
    level9 = [num_rows_9, num_columns_9, level9_grid, level9_psp, to_win_9, start_cost]
    levels.put(level9)

    # creating level 10
    level10_grid = [[3, 2, 2],
                    [2, 2, 3]]
    num_rows_10 = len(level10_grid)
    num_columns_10 = len(level10_grid[0])
    level10_psp = [(1, 0)]
    to_win_10 = 14
    level10 = [num_rows_10, num_columns_10, level10_grid, level10_psp, to_win_10, start_cost]
    levels.put(level10)

    # creating level 11
    # there are two players
    level11_grid = [[1, 1, 1, -1, -1],
                    [2, 1, 2, 1, 1],
                    [1, 1, 1, 1, 1]]
    num_rows_11 = len(level11_grid)
    num_columns_11 = len(level11_grid[0])
    level11_psp = [(0, 0), (1, 4)]
    to_win_11 = 15
    level11 = [num_rows_11, num_columns_11, level11_grid, level11_psp, to_win_11, start_cost]
    levels.put(level11)

    # creating level 12
    level12_grid = [[3, 3],
                    [2, 2],
                    [3, 3],
                    [2, 2]]
    num_rows_12 = len(level12_grid)
    num_columns_12 = len(level12_grid[0])
    level12_psp = [(0, 0)]
    to_win_12 = 20
    level12 = [num_rows_12, num_columns_12, level12_grid, level12_psp, to_win_12, start_cost]
    levels.put(level12)

    # creating level 13
    # There are Two players
    level13_grid = [[-1, -1, 1, -1],
                    [2, 2, 1, -1],
                    [2, 1, 2, 1],
                    [1, -1, 2, 1]]
    num_rows_13 = len(level13_grid)
    num_columns_13 = len(level13_grid[0])
    level13_psp = [(1, 2), (2, 0)]
    to_win_13 = 16
    level13 = [num_rows_13, num_columns_13, level13_grid, level13_psp, to_win_13, start_cost]
    levels.put(level13)

    # creating level 14
    level14_grid = [[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 2, 1]]
    num_rows_14 = len(level14_grid)
    num_columns_14 = len(level14_grid[0])
    level14_psp = [(0, 1), (1, 3)]
    to_win_14 = 13
    level14 = [num_rows_14, num_columns_14, level14_grid, level14_psp, to_win_14, start_cost]
    levels.put(level14)
