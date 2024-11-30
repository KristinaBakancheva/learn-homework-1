"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {}
questions_and_answers["как дела"] = "Хорошо!"
questions_and_answers["что делаешь?"] = "Программирую"

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    while True:
        question = input("Задайте свой вопрос.   ")
        if answers_dict.get(question.lower()) != None:
            print(answers_dict.get(question.lower()))
        else:
            print( "Пока =)")
            break




    
if __name__ == "__main__":
    ask_user(questions_and_answers)
