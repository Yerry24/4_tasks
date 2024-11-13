immutable_var = (1,2,"apple",'nut',[1,3])
print(immutable_var)
#immutable_var [0] = 2 так нельзя менять ибо 'tuple' object does not support item assignment
#immutable_var [2][0] = 'A'  так тоже нельзя менять ибо 'tuple' object does not support item assignment
immutable_var [4][0] = 'A' # а так можно изменить
print(immutable_var)
mutable_list = [22,33,'peach',[44,55]]
print(mutable_list)
mutable_list [0] = 66
print(mutable_list)