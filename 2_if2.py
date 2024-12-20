"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка "learn", возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def compare_str(str1, str2):
    result = set()
    if not isinstance(str1, str) or not isinstance(str2, str): # not isinstanse(str1, str) or not isinstanse(str2, str)
        result.add(0)
        return result
    elif str1 == str2:
         result.add(1)
    elif str2 == "learn":
         result.add(3)
    if len(str1) > len(str2):
         result.add(2)
    return result

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    print(compare_str(1, "love")) #0 - первый параметр не строка
    print(compare_str("1", 12)) #0 - второй параметр не строка
    print(compare_str("love", "love")) #1 - одинаковые
    print(compare_str("love", "toy")) #2 - первая строка длинее 
    print(compare_str("toy", "learn")) #3 - вторая строка = "learn"
    print(compare_str("animals", "learn")) #2,3 - первая строка длинее и вторая строа =
                                          #"learn"(в задании не было уточнения что такого быть не может)


    

    
if __name__ == "__main__":
    main()
