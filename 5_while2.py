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
questions_and_answers["Как дела"] = "Хорошо!"
questions_and_answers["Что делаешь?"] = "Программирую"

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    question = input('Задайте свой вопрос.   ')
    while len(question) > 0 and question.lower() != 'выход':
        if questions_and_answers.get(question) != None:
            print(questions_and_answers.get(question))
        else:
            print('Записи нет')
        next = input('Хотите задать еще вопрос?   ')
        if next.lower() == 'да':
            question = input('Задайте свой вопрос.   ')
        else:
            return 'Пока =)'




    
if __name__ == "__main__":
    ask_user(questions_and_answers)
