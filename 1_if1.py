"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

#задала как параметр так как в какой-то момент возможно нужно будет это поменять 
#и не нужно вычитывать код что б найти место для замены
max_age = 120 
school_age = 7
university_age = 19
work_age = 24


def check_occupation(age):
    if age < school_age:
        return "учится в детском саду"
    elif age >= school_age and age < university_age:
        return "учится в школе"
    elif age >= university_age and age < work_age:
        return "учится в ВУЗе"
    else:
        return "работает"
        

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    user_age = input("Введите пожалуйста сколько вам полных лет?    ")
    while True:
        try:
            if int(user_age) > max_age or int(user_age) <=0:
                user_age = input(f"Вы ввели некорректное значение возраста. \
                                 Возраст должен быть числом больше 0 и меньше {max_age}. \
                                 Введите пожалуйста сколько вам полных лет?    ")
            else:
                break

        except ValueError:
            user_age = input(f"Вы ввели некорректное значение возраста. \
                             Возраст должен быть числом больше 0 и меньше {max_age}. \
                             Введите пожалуйста сколько вам полных лет?    ")


    occupation = check_occupation(int(user_age))
    print(f"Возраст пользователя - {user_age}, род деятельности - {occupation}.")

if __name__ == "__main__":
    main()
