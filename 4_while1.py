"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    """
    Замените pass на ваш код
    """
    answer = input("Привет! Как дела?    ")
    while answer.lower() != "хорошо":
        answer = input("А ещё?    ")
    print("Пока =)")
    
if __name__ == "__main__":
    hello_user()
