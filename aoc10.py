import math
from collections import deque

stack = deque()

def main():
    with open('input.txt', 'r') as file:
        inputs = file.readlines()
        values = []
        for val in inputs:
            values.append(val.strip('/n'))
        row = len(values[0])
        col = len(values)
        curr_elem = inputs[0][0]
        if can_move_left(0, 0, values, curr_elem):
            stack.append(curr_elem)
            stack.append(values[row][col - 1])
            i = row
            j = col - 1

        if can_move_right(0, 0, values, row, curr_elem):
            stack.append(values[row][col + 1])
            i = row
            j = col + 1
        if can_move_down(0, 0, values, curr_elem, row):
            stack.append(values[row + 1][col])
            i = row + 1
            j = col
        if can_move_up(0, 0, values, curr_elem):
            stack.append(values[row - 1][col])
            i = row - 1
            j = col


def run_again(i, j, row, col, values):
    curr_elem = values[i][j]
    if can_move_left(i, j, values, curr_elem):
        stack.append(curr_elem)
        stack.append(values[row][col - 1])
        i = row
        j = col - 1
        run_again(i, j, row, col, values)

    if can_move_right(i, i, values, row, curr_elem):
        stack.append(values[row][col + 1])
        i = row
        j = col + 1
        run_again(i, j, row, col, values)
    if can_move_down(i, j, values, curr_elem, row):
        stack.append(values[row + 1][col])
        i = row + 1
        j = col
        run_again(i, j, row, col, values)
    if can_move_up(i, j, values, curr_elem):
        stack.append(values[row - 1][col])
        i = row - 1
        j = col
        run_again(i, j, row, col, values)


def can_move_left(row, col, values, curr_elem) -> bool:
    return col - 1 > 0 and values[row][col - 1] is not None and abs(values[row][col] - curr_elem) == 1


def can_move_right(row, col, values, row_length, curr_elem) -> bool:
    return col + 1 < row_length and values[row][col + 1] is not None and abs(values[row][col + 1] - curr_elem) == 1


def can_move_down(row, col, values, curr_val, row_length) -> bool:
    return row + 1 < row_length and values[row + 1][col] is not None and abs(values[row + 1][col] - curr_val) == 1


def can_move_up(row, col, values, curr_val) -> bool:
    return row - 1 > 0 and values[row - 1][col] is not None and abs(values[row - 1][col] - curr_val) == 1


if __name__ == '__main__':
    main()