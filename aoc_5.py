def main()->None:
    rules = {}
    input_to_test = []
    with open('input5.txt') as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            if "|" in line:
                print(line.strip('\n'))
                curr_line = line.strip('\n')
                values = curr_line.split("|")
                key = values[0]
                val = values[1]
                if key in rules:
                    cuur_val = rules[key]
                    a_list = list(cuur_val)
                    a_list.append(val)
                    tup = tuple(a_list)
                    rules[key] = tup
                else:
                    tup = (val,)
                    rules[key] = tup
            elif line == "\n":
                continue        
            else:
                print("not rule",line.strip('\n'))
                input =line.strip('\n')
                input_to_test.append(input)
    print(rules)
    print(input_to_test)
    idx = 0
    setty = set()
    sum = 0
    for inp in input_to_test:
        
        elems = inp.split(",")
        print(len(elems))
        mid = 0
        if len(elems) % 2 != 0:
            mid = int(elems[len(elems) // 2])
        else:
            mid = int(elems[len(elems)//2])  +   int(elems[(len(elems)// 2)  -1])
        i = 0
        is_complete = False
        while i < len(elems):
            res = elems[i+1:]
            if elems[i] in rules:
                found_elem = list(rules[elems[i]])
                missing_item = [x for x in res if x not in found_elem]
                if len(res) == 0:
                     val = elems [i-1:i]
                     oops_elem = [x for x in val if x in found_elem]
                     if len(oops_elem) >= 1:
                         setty.add(idx)
                         is_complete = False
                         print(elems[i], oops_elem[0])
                         break
                elif len(missing_item) >= 1:
                    setty.add(idx)
                    is_complete = False
                    print(elems[i], missing_item[0])
                    break
                else:
                    is_complete = True
    

                
                    

                              
                
            i =i+1
        if is_complete :
            sum = sum + mid           
        idx =idx+1    

  
    print(sum)




if __name__ =='__main__':
    main()