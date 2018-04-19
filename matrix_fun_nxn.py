nrows = int(input("Enter number of rows in matrix: "))
ncols = int(input("Enter number of columns in matrix: "))

matrix = {}
for r in range(nrows):
	row_vals = input("Enter %d numbers in matrix row #%d separated by spaces: " %(ncols, r+1))
	#val_num = [int(v) for v in row_vals.split()]
	matrix[r+1] = tuple([int(v) for v in row_vals.split()])

print(matrix)


#val_num = [int(v) for v in val_str.split()]
#matrix = ((val_num[0], val_num[1]),(val_num[2], val_num[3]))
#inv_factor = 1/(val_num[0]*val_num[3] - val_num[1]*val_num[2])
#inverse = ((inv_factor*val_num[3],-1*inv_factor*val_num[1]),(-1*inv_factor*val_num[2], inv_factor*val_num[0]))
#print("matrix:", matrix)
#print("inverse:", inverse)