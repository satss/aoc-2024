from collections import deque 


def main()-> int:
    leftli: list[int] = []
    rightli: list[int]= []
    unsafeCounter = 0
    total_size = 0
    with open('input.txt') as f:
        lines = f.readlines()
        total_size = len(lines)
        for elem in lines:
            level = 0;
            values = elem.strip('\n').split(" ")
            first_elem = int(values[0])
            seconf_elem = int(values[1])
            is_decreasing = False
            if first_elem > seconf_elem:
                is_decreasing = True
            for i in range(len(values)):
                if i != 0:
                    curr_val = int(values[i])

                    if is_decreasing  and first_elem < curr_val and level > 0:
                        unsafeCounter = unsafeCounter +1
                        print(elem)
                        break

                    elif is_decreasing  and first_elem < curr_val and level == 0:
                        level = level +1

                    elif not is_decreasing  and first_elem > curr_val  and level > 0:
                        unsafeCounter = unsafeCounter +1
                        print(elem)
                        break    


                    
                    elif not is_decreasing  and first_elem > curr_val  and level == 0:
                        level = level +1

                    elif first_elem == curr_val and level > 0:
                        unsafeCounter = unsafeCounter +1
                        print(elem)
                        break

                    elif first_elem == curr_val and level == 0:
                        level = level +1


                    elif first_elem > curr_val and is_decreasing:
                        if abs(first_elem-curr_val) >=1 and abs(first_elem-curr_val) <=3:
                            first_elem =curr_val
                        else:
                            if abs(first_elem-curr_val) >=4 and level  > 0: 
                                unsafeCounter = unsafeCounter +1
                                print(elem)
                                break
                            elif abs(first_elem-curr_val) >=4 and level == 0:
                                if i == len(elem)-1 or i == 0:
                                    level = level+1  
                                else:
                                    unsafeCounter = unsafeCounter +1
                                    print(elem)
                                    break
                            else:
                                if level  == 0:
                                    level = level +1
                                else:
                                    unsafeCounter = unsafeCounter +1
                                    print(elem)
                                    break               



                    elif first_elem < curr_val and not is_decreasing:
                        if abs(curr_val- first_elem) >=1 and abs(curr_val- first_elem) <=3:
                                first_elem =curr_val
                        else:
                            if abs(curr_val-first_elem) >=4 and level  > 0: 
                                unsafeCounter = unsafeCounter +1
                                print(elem)
                                break
                            elif abs(curr_val-first_elem) >=4 and level == 0:
                                if i == len(values)-1 or i == 0:
                                    level = level+1  
                                else:
                                    unsafeCounter = unsafeCounter +1
                                    print(elem)
                                    break     
                            else:
                                if level  == 0:
                                    level = level +1
                                else:
                                    unsafeCounter = unsafeCounter +1
                                    print(elem)
                                    break  

    return total_size - unsafeCounter                     
                

def dampner(elems: list[int], is_decreasing:bool)->int:
    stack = deque()
    unsafe_amount = 0
    cnt = 0
    for elem in elems:
        if cnt == 0:
            stack.append(elem)
        else:
            if elem > stack.peek() and not is_decreasing and abs(elem - stack.peek()) >=4:
                unsafe_amount = unsafe_amount +1

                
        


        cnt = cnt +1    



    return 0

if __name__ == "__main__":
    print("result",main())