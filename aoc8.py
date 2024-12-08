
char_found  = set()
dic = dict()
antinodes = []

def is_within_boundary_nonblocked(dic, row_len, col_len, no_antinodes)-> int:
   for key in dic.keys():
        values= dic[key]
        for i in range(0, len(values)):
           row, col = values[i]
           for j in range(i+1, len(values)):
              row2, col2= values[j]
              diff_row = row2-row
              diff_col = col2-col
              first_antinode_row =  row -diff_row
              first_antinode_col =col - diff_col

              second_antinode_row = diff_row + row2
              second_antinode_col = diff_col + col2
              is_antinode_one = within_grid(row_len, col_len, first_antinode_row, first_antinode_col)
              is_antinodes_two =within_grid(row_len, col_len, second_antinode_row, second_antinode_col)
              if is_antinode_one:
                 print("antinode",first_antinode_row, first_antinode_col)
                 no_antinodes= no_antinodes+1
                 antinodes.append((first_antinode_row, first_antinode_col))
              if is_antinodes_two:
                 print("antinode",second_antinode_row, second_antinode_row)
                 no_antinodes = no_antinodes+1  
                 antinodes.append((second_antinode_row, second_antinode_col))
                 print("\n")
   return no_antinodes              



def within_grid(row_len, col_len, row, col):
   if row >= 0 and row < row_len and col >= 0 and col < col_len:
      return True
   return False

def main():
  no_antinodes = 0
  with open("input8.txt", "r") as file:
     f = file.readlines()
     print(f)
     row_len = len(f)
     col_len = len(f[0].strip("\n"))
     print("row-length", row_len)
     print("col.length", col_len)
     for i in range(0, row_len):
        for j in range(0, col_len):
           if str(f[i][j]) != ".":
              print(f[i][j], i, j)
              if f[i][j] not in dic:
                 print(f[i][j])
                 li = []
                 li.append((i,j))
                 dic[f[i][j]] = li
              else:
                 val = dic[f[i][j]]
                 val.append((i,j))
                 dic[f[i][j]] = val
     print("dic",dic)
  res = is_within_boundary_nonblocked(dic=dic, row_len=row_len, col_len=col_len,no_antinodes=no_antinodes)   
  print("no_antinodes",res)     
  print(antinodes)

  set_oftup =set()
  for elem in antinodes:
     set_oftup.add(elem)
  print(len(set_oftup))   
     


if __name__ =="__main__":
    main()
