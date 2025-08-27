# 0   1  2    3


# var_list1 = [12, 0, 16, 8, '1234', -100, True]  # массив переменных
#
# for list_element in var_list1:
#     print('element:', var_list1.index(list_element), type(list_element), list_element)


# цикл, который итерируется по массиву объектов
# и берет каждый цикл себе в переменную (list_element)
# for list_element in (12, 16, 8, -100):
#     for list_element1 in var_list1:
#         print('element:', var_list1.index(list_element), type(list_element), list_element)
#     # kod do cikla
#     for list_element1 in var_list1:
#         # kod v cikle
#         print('element:', var_list1.index(list_element1), type(list_element1), list_element1)
#     # kod posle cikla

# var_int1 = 12
# while var_int1:
#     var_int1 = var_int1 - 1
#     print(var_int1)

# print('цикл завершен!')

# var_int2 = 12
# while var_int2 < 56:
#     var_int1 = var_int2 + 1
#     # print(var_int2)
#     if var_int2 == 56:
#         print('end')
#
# print('цикл завершен!')


# list_1 = ['Астана', 'Караганда', 'Чимкент', 'Актюбинск']
#
# index_i = 0
# for i in list_1:
#     print(i + " " + str(list_1.index(i) + 1))
# index_i += 1
# string_city = f"{i} {list_1.index(i) + 1}"
# print(string_city)
# # print('i' + " " + str(list_1.index('i') + 1))
#
#
# # TODO циклы
# for i in [2, 3, 4, 5, 6]:
#     print(i)
#
# str_value_1 = "Many яблок"
#
# for char_element in str_value_1:
#     print(char_element)
#
# print('разделение')
#
# str_value_2 = [[2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6]]
# for first_loop in str_value_2:
#     print(first_loop)
#     for second_loop in first_loop:
#         print(second_loop)
#
# while_continue = True
# index = 0
# while while_continue:
#     index = index + 2
#     print(index)
#     # index += 2
#     if index >= 30:
#         # break
#         while_continue = False
# print("#############################")
# # # практическое задание с циклами 1
# list_2 = [input('введите число 1: '), input('введите число 2: ')]
#
# for i in list_2:
#     print(i)
#
# # практическое задание с циклами 2
# list_3 = [input('введите число 1: '), input('введите число 2: ')]
# # list_3 = [15, 14]
# for i in list_3:
#     if int(i) % 2 != 0:
#         print(str(i) + ' ' + 'нечетное число')
#
# # практическое задание с циклами 3
# list_4 = [input('введите число 1: '), input('введите число 2: ')]
# # list_4 = [15, 14]
# for i in list_4:
#     if int(i) % 2 == 0:
#         print(str(i) + ' ' + 'четное число')

# практическое задание с циклами 4
# list_5 = [input('введите число 1: '), input('введите число 2: ')]
# list_5 = [43, 12]
# list_5 = [7, 3, 9, 2, 1]
#
# temp = 0
# for i in range(0, len(list_5)):
#     for j in range(i + 1, len(list_5)):
#         if list_5[i] > list_5[j]:
#             temp = list_5[i]
#             list_5[i] = list_5[j]
#             list_5[j] = temp
# print(list_5)


# практическое задание с циклами 5
# list_6 = [43, 11]
# list_6 = [7, 3, 9, 2, 1]
# list_6 = [input('введите число 1: '), input('введите число 2: ')]
# temp = 0
# for i in range(0, len(list_6)):
#     for j in range(i + 1, len(list_6)):
#         if list_6[i] > list_6[j]:
#             temp = list_6[i]
#             list_6[i] = list_6[j]
#             list_6[j] = temp
# print(list_6)
# for list_elem in list_6:
#     if int(list_elem) % 2 != 0:
#         print(str(list_elem) + ' ' + 'нечетное число')


var_list = ["Almaty", "Nur-sultan", "Taras", "Ekebaztuz"]

index_i = 0

for i in var_list:
    string_city = f"{i} {index_i + 1}"

    # print(i + " " + str(var_list.index(i) + 1))
    print(string_city)
    index_i += 1