
from enum import Enum
class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT  = "right"

curr_pos = 0


def canGo():
    pass

def main():
    blockers = dict()
    with open('input_6.txt') as f:
        lines = f.readlines()
        print(lines)
        colum_cnt= len(lines[0].strip("\n"))
        print(colum_cnt)
        start_pos= 0
        direction = Direction.UP
        curr_row = 0

        for lin in lines:
            print(lin.strip('\n'))
            str_line = lin.strip('\n')
            i = 0
            
            for char in str_line:
                if char == '#':
                    curr_key = curr_row * 10 + i
                    blockers.update({curr_key: "#"})
                    i = i +1;
                elif char == '^':
                    start_pos = curr_row *10 + i;
                    i = i +1;    
                else:
                    i = i +1;   
            curr_row = curr_row +1 
        print("blockers",blockers)
        print("start position",start_pos)
        print("diretion", direction)
        print(curr_row)
    curr_pos = start_pos
    num_rows = curr_row
    while True:
        if direction.name == Direction.UP:
            may_be_po = curr_pos - num_rows
            if may_be_po in blockers:
                direction = Direction.RIGHT
                may_be_po_1 = curr_pos+1
                if may_be_po_1 in blockers:
                    direction = Direction.DOWN
                    may_be_po_2 = curr_pos + num_rows
                    if may_be_po_2 in blockers:
                        direction = Direction.LEFT
                        may_be_po_3 = curr_pos -1
                        if may_be_po_3 in blockers:
                            print("blocked from all sides") 
            else:
                curr_pos = curr_pos - num_rows                   

if __name__ == '__main__':
    main()