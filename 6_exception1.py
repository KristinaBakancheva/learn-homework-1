"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    answer = input('Привет! Как дела?    ')
    while answer.lower() != 'хорошо':
        
        try:
            answer = input('А ещё?(Если хотите выйти нажми Cntr + C)    ')
        except KeyboardInterrupt:
            print("Пока.")
            break
    
if __name__ == "__main__":
    hello_user()
