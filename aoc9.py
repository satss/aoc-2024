from collections import deque
stack = deque()


def main():
    input = ""
    with open("input9.txt", "r") as file:
     input = file.readlines()
    type_of= 'file'
    file_id= 0
    stack = deque()
    res =""
    for elm in input[0]:
        if type_of == 'file':
            val = [file_id] * int(elm) 
            res =res+"".join(str(x) for x in val)
            for x in val:
                stack.append(str(x))
            file_id = file_id+1
            type_of ='disk'
        else:
            val = ['.'] * int(elm) 
            res= res +"".join(x for x in val)
            for x in val:
                stack.append(str(x))
            type_of ='file'
    print("res",res)
    print("stack", stack)
    resstack = deque()
    while len(stack) != 0:
        elem = stack.popleft()
        if elem == '.':
            while len(stack) > 0 and stack[len(stack)-1] == '.':
                stack.pop()

            if len(stack) > 0:
                resstack.append(int(stack.pop()))
        elif elem.isdigit():
            resstack.append(int(elem))
    print("restack", resstack)

    checksum_res = 0
    file_id_cnter =0 

    while len(resstack) != 0:
        var = file_id_cnter * resstack.popleft()
        checksum_res = checksum_res + var
        file_id_cnter = file_id_cnter +1
    print("checksum_res", checksum_res)    

  
   




if __name__=='__main__':
    main()