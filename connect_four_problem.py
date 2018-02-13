import random


def run_game(game_type, blocked_cells, player_inputs):
    num = 5
    grid = [[['O'], ['O'], ['O'], ['O'], ['O']],
            [['O'], ['O'], ['O'], ['O'], ['O']],
            [['O'], ['O'], ['O'], ['O'], ['O']],
            [['O'], ['O'], ['O'], ['O'], ['O']],
            [['O'], ['O'], ['O'], ['O'], ['O']]]
    print_grid(grid)

    player_a = ['A']
    player_b = ['B']
    blocked_value = ['X']
    player_computer = ['C']

    computer_as_one_player = False

    game_type_split = game_type.split('-')

    if game_type_split[0] == 'COMPUTER' or game_type_split[1] == 'COMPUTER':
        computer_as_one_player = True

    for each_blocked_cell in blocked_cells:
        row_index = each_blocked_cell[0] - 1
        column_index = each_blocked_cell[1] - 1

        grid[row_index][column_index] = blocked_value
        while row_index != num - 1:
            row_index += 1
            grid[row_index][column_index] = blocked_value

    print_grid(grid)

    if not computer_as_one_player:
        for each_input in player_inputs:
            if each_input[0] == 'A':
                _value = player_a
            elif each_input[0] == 'B':
                _value = player_b

            status = push_the_ball(grid, each_input[1], num, _value)
            print_grid(grid)

            if status:
                return
    else:
        for each_input in player_inputs:
            status = push_the_ball(grid, each_input[1], num, player_a)
            print_grid(grid)

            if status:
                return

            status = push_the_ball(grid, random.randint(1, 5), num, player_computer)
            print_grid(grid)

            if status:
                return


def push_the_ball(grid, each_input, num, value):
    column_input = each_input - 1
    temp_row = num - 1

    while temp_row != -1:
        if grid[temp_row][column_input] == ['O']:
            grid[temp_row][column_input] = value
            break
        else:
            temp_row -= 1

    if temp_row == -1:
        print "{} Column full!".format(each_input)

    success = check_if_anybody_won(grid, temp_row, column_input, value, num)

    return success


def check_if_anybody_won(grid, row, column, value, num):
    # check for column matching
    success = check_columns(row, column, num, grid, value)

    if success:
        return True

    # check for rows matching
    success = check_rows(row, column, num, grid, value)

    if success:
        return True

    # check for diagonal matching
    success = check_diagonals(row, column, num, grid, value)

    if success:
        return True

    return False


def check_columns(t_row, column, num, grid, value, ):
    cells_list = []
    if grid[1][column] != value or grid[2][column] != value or grid[3][column] != value:
        return False

    while t_row != num:
        if grid[t_row][column] == value:
            cells_list.append((t_row+1, column+1))
        else:
            return False

        t_row += 1

        if len(cells_list) == 4:
            print_winner(cells_list, value)
            return True

    return False


def check_rows(row, column, num, grid, value):
    cells_list = []
    # check for row matching
    if grid[row][1] != value or grid[row][2] != value or grid[row][3] != value:
        return False
    else:
        t_column = 0
        while t_column != num:
            if grid[row][t_column] == value:
                cells_list.append((row+1, t_column+1))
            t_column += 1

            if len(cells_list) == 4:
                print_winner(cells_list, value)
                return True

    return False

def check_diagonals(row, column, num, grid, value):
    cells_list = []
    
    status = check_opposite_diagonals(check_opposite_diagonals)
    if status:
        return True
    
    if row == column:
        if grid[1][1] != value or grid[2][2] != value or grid[3][3] != value:
            return False
        else:
            for i, j in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]:
                if grid[i][j] == value:
                    cells_list.append((i+1, j+1))

                if len(cells_list) == 4:
                    print_winner(cells_list, value)
                    return True

    elif row > column and (row, column) in [(1, 0), (2, 1), (3, 2), (4, 3)]:
        for i, j in [(1, 0), (2, 1), (3, 2), (4, 3)]:
            if grid[i][j] == value:
                cells_list.append((i+1, j+1))
            else:
                return False

            if len(cells_list) == 4:
                print_winner(cells_list, value)
                return True
    elif column > row and (row, column) in [(0, 1), (1, 2), (2, 3), (3, 4)]:
        for i, j in [(0, 1), (1, 2), (2, 3), (3, 4)]:
            if grid[i][j] == value:
                cells_list.append((i+1, j+1))
            else:
                return False

            if len(cells_list) == 4:
                print_winner(cells_list, value)
                return True

    return False

def check_opposite_diagonals(row, column, num, grid, value):
    if (row, column) in [(3, 0), (2, 1), (1, 2), (0, 3)]:
        for i, j in [(3, 0), (2, 1), (1, 2), (0, 3)]:
            if grid[i][j] == value:
                cells_list.append((i+1, j+1))
            else:
                return False

            if len(cells_list) == 4:
                print_winner(cells_list, value)
                return True
    elif (row, column) in [(4, 1), (3, 2), (2, 3), (1, 4)]:
        for i, j in [(4, 1), (3, 2), (2, 3), (1, 4)]:
            if grid[i][j] == value:
                cells_list.append((i+1, j+1))
            else:
                return False

            if len(cells_list) == 4:
                print_winner(cells_list, value)
                return True
    elif (row, column) in [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]:
        if grid[3][1] != value or grid[2][2] != value or grid[1][3] != value:
            return False
        else:
            for i, j in [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]:
                if grid[i][j] == value:
                    cells_list.append((i+1, j+1))

                if len(cells_list) == 4:
                    print_winner(cells_list, value)
                    return True

def print_winner(cells_list, value):
    print "Cells part of winning line - {}".format(cells_list)
    print 'FinalGameResult: {} wins'.format(value[0])


def print_grid(grid):
    for i in xrange(5):
        print grid[i]
    print "\n\n\n"


def start_game(game_type, blocked_cells, player_inputs):
    try:
        run_game(game_type, blocked_cells, player_inputs)
    except IndexError:
        print "Calm down you're going out of range!"


if __name__ == "__main__":
    game_type, blocked_cells, player_inputs = 'HUMAN-HUMAN', \
                                              [(2,2), (3,4)], \
                                              [('A', 5), ('B',4), ('A', 5), ('B', 1), ('A', 5), ('B', 1), ('A', 5)]

    start_game(game_type, blocked_cells, player_inputs)


