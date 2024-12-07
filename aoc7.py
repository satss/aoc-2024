import math


def mul(nums:list[int])-> int:
    res = nums[0]
    for i in range(nums.count()):
        if i != 0:
            res = res * nums[i]
    return res


def add(nums:list[int])-> int:
    res = nums[0]
    for i in range(nums.count()):
        if i != 0:
            res = res  + nums[i]
    return res

def add_nums_acc_comb(nums:list[int], target:int, operands_com : str)-> int:

    res = nums[0]
    tup_counter = 0
    print(operands_com)
    for j in range(1,len(nums)):
            for el in range(tup_counter, len(operands_com)) :
                    print(operands_com[el])
                    if operands_com[el] == '0':
                        res = res + nums[j]
                        break
                    
                    if operands_com[el] =='1':
                        res = res * nums[j]
                        break
            tup_counter = tup_counter +1     
    return res           





                
 
 
        





def main():
    results = []
    with open('input7.txt', 'r') as f:
        out = f.readlines()
        for i in out :
            val = i.strip('\n')
            values = val.split(":")
            target = int(values[0])
            numszt = values[1].lstrip().split(" ")
            total_nums =len(numszt)
            operands = total_nums -1
            #combinations  = math.power(total_nums,operands)
            nums = []
            for el in numszt:
                nums.append(int(el))

            list_com = []    
            for i in range(1 << operands):
                bin_str = format(i, '0'+ str(operands) + 'b')
           
                list_com.append(bin_str)
            for el in list_com:
                val = add_nums_acc_comb(nums=nums,target=target,operands_com=el)
                if val == target:
                    results.append(val)
                    break


    print(results)   
    sum = 0
    for el in results :
        sum = sum + el
    print(sum)    




if __name__=='__main__':
    main()