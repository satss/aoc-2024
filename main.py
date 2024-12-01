

def main()-> None:
    leftli: list[int] = []
    rightli: list[int]= []
    with open('input.txt') as f:
        lines = f.readlines()

        for elem in lines:
            values =elem.split("   ")
            leftli.append(int(values[0]))
            rightli.append(int(values[1].strip("\n")))
    print(leftli)
    print(rightli)
    similarity_score(leftli=leftli, rightli=rightli)
    cnt = len(leftli)
    sum = 0
    while (cnt > 0):
            smalles_elem_li = min(leftli)
            print(smalles_elem_li)    
            leftli.remove(smalles_elem_li)
            print("after removal",leftli)

            smalles_elem_ri = min(rightli)
            print(smalles_elem_ri)    
            sum = sum + abs(smalles_elem_li-smalles_elem_ri)
            rightli.remove(smalles_elem_ri)
            print("after removal",rightli)
            cnt =cnt -1
    print(sum)        


def similarity_score(leftli: list[int], rightli: list[int])->None:
    sum = 0
    for elem in leftli:
          occ = rightli.count(elem)
          sum = sum + (elem * occ)
    print("similarity score",sum)      
        


if __name__ == "__main__":
    main()