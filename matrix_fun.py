val_str = input("Enter 4 numbers separated  by spaces: ")
val_num = [int(v) for v in val_str.split()]
matrix = ((val_num[0], val_num[1]),(val_num[2], val_num[3]))
inv_factor = 1/(val_num[0]*val_num[3] - val_num[1]*val_num[2])
inverse = ((inv_factor*val_num[3],-1*inv_factor*val_num[1]),(-1*inv_factor*val_num[2], inv_factor*val_num[0]))
print("matrix:", matrix)
print("inverse:", inverse)