
print("Операторы:")
print("+  -  *  /  //  %  **")
print("==  !=  >  <  >=  <=")
print("and  or  not")
print("&  |  ^  ~  <<  >>")
print("in  not in")
print("is  is not")
print("-" * 40)

my_list = [0,1,2,3,4,5,6,7,8,9]

try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    op = input("Введите оператор: ")

    if op == "+":
        print("Сумма:", num1 + num2)
    elif op == "-":
        print("Разность:", num1 - num2)
    elif op == "*":
        print("Произведение:", num1 * num2)
    elif op == "/":
        if num2 == 0:
            print("Ошибка: деление на 0")
        else:
            print("Частное:", num1 / num2)
    elif op == "//":
        if num2 == 0:
            print("Ошибка: деление на 0")
        else:
            print("Целая часть от деления:", num1 // num2)
    elif op == "%":
        if num2 == 0:
            print("Ошибка: деление на 0")
        else:
            print("Остаток от деления:", num1 % num2)
    elif op == "**":
        print("Степень:", num1 ** num2)

    elif op == "==":
        print("Равны?", num1 == num2)
    elif op == "!=":
        print("Не равны?", num1 != num2)
    elif op == ">":
        print("Первое больше второго?", num1 > num2)
    elif op == "<":
        print("Первое меньше второго?", num1 < num2)
    elif op == ">=":
        print("Первое больше или равно второму?", num1 >= num2)
    elif op == "<=":
        print("Первое меньше или равно второму?", num1 <= num2)

    elif op == "and":
        print("Логическое И:", bool(num1) and bool(num2))
    elif op == "or":
        print("Логическое ИЛИ:", bool(num1) or bool(num2))
    elif op == "not":
        print("not", num1, "->", not bool(num1))
        print("not", num2, "->", not bool(num2))

    elif op == "&":
        print("Побитовое И:", num1 & num2)
    elif op == "|":
        print("Побитовое ИЛИ:", num1 | num2)
    elif op == "^":
        print("Побитовое XOR:", num1 ^ num2)
    elif op == "~":
        print("Побитовое НЕ:", ~num1)
    elif op == "<<":
        print("Сдвиг влево:", num1 << num2)
    elif op == ">>":
        print("Сдвиг вправо:", num1 >> num2)

    elif op == "in":
        if num1 in my_list:
            print(num1, "есть в списке")
        else:
            print(num1, "нет в списке")

        if num2 in my_list:
            print(num2, "есть в списке")
        else:
            print(num2, "нет в списке")

    elif op == "not in":
        if num1 not in my_list:
            print(num1, "не входит в список")
        else:
            print(num1, "входит в список")

        if num2 not in my_list:
            print(num2, "не входит в список")
        else:
            print(num2, "входит в список")

    elif op == "is":
        if num1 is num2:
            print("Объекты тождественны")
        else:
            print("Объекты не тождественны")
    elif op == "is not":
        if num1 is not num2:
            print("Объекты нетождественны")
        else:
            print("Объекты тождественны")
    else:
        print("Такого оператора нет")

except ValueError:
    print("Извините, произошла ошибка")
