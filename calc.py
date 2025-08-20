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
