from collections import deque
import math


def main():
    inputs = "4189 413 82070 61 655813 7478611 0 8"
    integers = inputs.split(" ")
    result = ""
    for val in integers:
        if int(val) == 0:
            # give 1
            result = result+ str("1") + " "

        elif len(val) % 2 != 0:
            val_int = int(val)
            res = val_int * 2024            
            result = result+ str(res) + " "
        elif len(val) % 2 == 0:
            mid = len(val)//2
            first_half = val[:mid].lstrip('0')
            if is_all_zero(val=first_half):
                first_half = '0'
            second_half = val[mid:].lstrip('0')
            if is_all_zero(val=second_half):
                second_half = '0'
            result = result+ first_half +  " " + second_half + " "

        else:
            raise ValueError("rule not found") 
    print(result)
    cnter = 24

    while cnter >0:
        relt_str = blink_it_away(result)
        cnter =cnter -1
        result =relt_str
    
    print(relt_str)
    print("\n")
    print(result)
    new_res= result.rstrip(" ")
    loop_over =new_res.split(" ")
    result_length = 0
    for el in loop_over:
        result_length = result_length +1
    print(result_length)    

               

def blink_it_away(input)->str:
    result = ""
    integers = input.rstrip(" ").split(" ");
    for val in integers:

        if int(val) == 0:
            # give 1
            result = result+ str("1") + " "
        elif len(val) % 2 != 0:
            val_int = int(val)
            res = val_int * 2024            
            result = result+ str(res) + " "
        elif len(val) % 2 == 0:
            mid = len(val)//2
            first_half = val[:mid].lstrip('0')
            if is_all_zero(val=first_half):
                first_half = '0'
            second_half = val[mid:].lstrip('0')
            if is_all_zero(val=second_half):
                second_half = '0'
            result = result+ first_half +  " "+ second_half + " "
        else:
            raise ValueError("rule not found") 
    return result    

    


def is_all_zero(val:str)-> bool:
    for el in val:
        if el != '0':
            return False
    return True    
if __name__=='__main__':
    main()