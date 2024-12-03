from re import finditer

from collections import deque

def main():
    
    lines = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    result : list[str] =[]

    stack = deque()




    for i in range(len(lines)):
        
        if lines[i] == 'm' and len(stack) == 0:
            k = i- 4
            l = i-6

            while k > 0 and k < i:
                if lines[k] == 'd':
                     stack.append('d')
                     k =k +1
                elif lines[k] == 'o':
                     stack.append('o')  
                     k = k+1
                elif lines[k] == '(':
                     stack.append('(')  
                     k = k+1 
                elif lines[k] == ')':
                     stack.append(')')  
                     k = k+1
                else:
                    while len(stack) != 0:
                        stack.pop()
                    k = k+1         
            while l > 0 and l < i:
                if lines[l] == 'd':
                     stack.append('d')
                     l =l +1
                elif lines[l] == 'o':
                     stack.append('o')  
                     l = l+1
                elif lines[l] == 'n':
                     stack.append('n')  
                     l = l+1   
                elif lines[l] == '\'':
                     stack.append('\'')  
                     l = l+1     
                elif lines[l] == 't':
                     stack.append('t')  
                     l = l+1           
                elif lines[l] == '(':
                     stack.append('(')  
                     l = l+1 
                elif lines[l] == ')':
                     stack.append(')')  
                     l = l+1
                else:
                    while len(stack) != 0:
                        stack.pop()
                    l =l+1

            stack.append('m')

        elif lines[i] == 'u' and len(stack) > 0 and stack[len(stack)-1] =='m':
            stack.append('u')  


        elif lines[i] == 'l' and len(stack) > 0 and stack[len(stack)-1] =='u':
            stack.append('l')        
       
        elif lines[i] == '(' and len(stack) > 0 and stack[len(stack)-1] =='l':
            stack.append('(')   
        
        elif str(lines[i]).isdigit() and len(stack) > 0 and (stack[len(stack)-1] == '(' or str(stack[len(stack)-1]).isdigit()):
            stack.append(lines[i])

        elif lines[i] == ',' and len(stack) > 0 and  str(stack[len(stack)-1]).isdigit():
            stack.append(lines[i])    


        elif str(lines[i]).isdigit() and len(stack) > 0 and   (stack[len(stack)-1] == ',' or str(stack[len(stack)-1]).isdigit()):
            stack.append(lines[i])

        elif lines[i] == ')' and len(stack) > 0 and  str(stack[len(stack)-1]).isdigit():
            stack.append(lines[i])  
            mulval = ""
            while len(stack) != 0:
                mulval = mulval + stack.popleft()
            result.append(mulval)    

        else:
            while len(stack) != 0:
                stack.pop()
            
    print(result)
    final_sum = 0
    for elem in result:
       try:
        seps = elem.split('(')
        di = seps[1].split(',')
        first_elm = int(di[0])
        second_elm = int(di[1][:-1])
        print(first_elm)
        final_sum = final_sum + (first_elm * second_elm)
        print(second_elm)
       except ValueError:
           print(elem) 
    print(final_sum)


            



    
  


if __name__ == '__main__':
    main()