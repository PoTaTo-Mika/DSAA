param = input()
param_list = [int(num) for num in param.split()]
matrix = []
for i in range(param_list[0]):
    number = input()
    matrix.append([int(num) for num in number.split()])
    