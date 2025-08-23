#  функция с заданными параметрами
#
# def calc(number1, number2=10, operation='+'):
#     # if operation == "+":
#         return number1 + number2

def calc(number1=10, operation='/', number2=3):
    if operation == "/":
        return number1 / number2


result = calc()
print(result)

result = calc(operation="/", number2=3, number1=10)  # именованные аргументы
print(result)


def calc(number1, number2, operations):
    if operations == "+":
        return number1 + number2
    if operations == "-":
        return number1 - number2
    if operations == "*":
        return number1 * number2
    if operations == "**":
        return number1 ** number2
    if operations == "/":
        if number2 != 0:
            return number1 / number2
        else:
            print('Error!')
            return print("на нуль делить нельзя!!!")
    if operations == "//":
        if number2 != 0:
            return number1 // number2
        else:
            print('Error!')
            return 0
    if operations == "%":
        if number2 != 0:
            return number1 % number2
        else:
            print('Error! вы ввели нуль')
            return 0


result = calc(5, 10, "+")
print(result)
result = calc(9, 6, "-")
print(result)
result = calc(2, 2, "*")
print(result)
result = calc(3, 2, "**")
print(result)
result = calc(33, 0, "/")
print(result)
result = calc(33, 2, "//")
print(result)
result = calc(33, 0, "%")
print(result)
