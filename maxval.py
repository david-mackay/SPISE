names= ['Jemma', 'Brittany', 'Keonna', 'Jynene', 'Hananel']
colours = ['green', 'purple', 'blue', 'blue', 'white']
colours_list = [[x] for x in colours]

my_dict = {}

for i in range(len(names)):
    my_dict[names[i]] = colours_list[i]

my_dict["Jynene"].append('red')
print(my_dict["Jynene"])
