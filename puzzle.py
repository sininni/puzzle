from typing import List

def horisontal_check(board: List[str]) -> bool:
    """
    Checks if there`re no similar numbers in the
    same line.
    >>> horisontal_check(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    True
    """
    for row in board:
        row = [sign for sign in row
               if sign != '*' and sign != ' ']
        if len(row) != len(set(row)):
            return False
    return True

def vertical_check(board: List[str]) -> bool:
    """
    Checks if there`re no similar numbers in the
    same column.
    >>> vertical_check(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    """
    horizontal_board = []
    for index in range(9):
        new_row = str()
        for row in board:
            new_row += row[index]
        horizontal_board.append(new_row)
    return horisontal_check(horizontal_board)

def similar_color_area_check(board: List[str]) -> bool:
    """
    Checks if there`re no similar numbers in the same
    color area.
    >>> similar_color_area_check(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    True
    """
    start_index = 4
    row_index = 0
    while start_index > -1:
        while row_index < 5:
            number_list = []
            for key in range(row_index, row_index+5):
                if board[key][start_index] != ' ':
                    number_list.append(board[key][start_index])
                elif key == row_index+4:
                    for index in range(start_index+1, start_index+5):
                        if board[row_index+4][index] != ' ':
                            number_list.append(board[row_index+4][index])
            if len(number_list) != len(set(number_list)):
                return False
            else:
                start_index -= 1
                row_index +=1
    return True

def validate_board(board: List[str]) -> bool:
    """
    Indicates if board (9x9) is ready for game by checking
    if it fits to all game rules:
    1. There`re no similar numbers in the same row.
    2. There`re no similar numbers in the same column.
    3. There`re no similar numbers in the same color
    area.
    If everything is okay, returns True, False otherwise.
    >>> validate_board(["**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"])
    False
    """
    while horisontal_check(board) and vertical_check(board)\
        and similar_color_area_check(board):
        return True 
    return False

if __name__=='__main__':
    from doctest import testmod
    testmod()