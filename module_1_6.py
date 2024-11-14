my_dict = {'Юрий': 1964,'Антон': 1972,'Ирина': 1961}
print(my_dict)
print(my_dict ['Юрий'])
print(my_dict.get ('Игорь'))
my_dict.update ({'Игорь':1964,'Ольга':1971})
print(my_dict.pop ('Игорь'))
print(my_dict)
my_set = {314,'Pi',6.28,1,2,1,2,6.28}
print(my_set)
my_set.update({4,5})
my_set.discard(314)
print(my_set)