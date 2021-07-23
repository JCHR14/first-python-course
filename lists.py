

my_list = ["manzanas", "banana", "fresas", "mangos"]
# my_list_2 = my_list.copy()
# my_list_2.append("jocote")
# my_list_2.insert(0, "jocote")

# my_list_3 = ['jocote', 'limon']
# my_list.insert(2, my_list_3)
# my_list.extend(my_list_3)
# print(my_list)

# my_list.remove('banana')
# deleted = my_list.pop(1)
# del my_list[0]
# my_list.sort(reverse=True)
# print(my_list)
# print(deleted)

# print(dir(my_list))

# for item in my_list:
#     print(item)
# print(my_list[-3])
# print(my_list[1:])
# print(dir(my_list))


search = 'man'
result = [item for item in my_list if search in item]

# result = []
# for item in my_list:
#     if search in item:
#         result.append(item)


print(result)