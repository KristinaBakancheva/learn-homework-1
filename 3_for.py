"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {"product": "iPhone 12", "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {"product": "Xiaomi Mi11", "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {"product": "Samsung Galaxy 21", "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
from collections import Counter

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sells_phone = [
    {"product": "iPhone 12", "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {"product": "Xiaomi Mi11", "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {"product": "Samsung Galaxy 21", "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}]

    all = 0
    len_all = 0
    for i in range(len(sells_phone)):
        product = sells_phone[i].get("product")
        items_sold= sum(sells_phone[i].get("items_sold"))
        avg_items_sold = round(sum(sells_phone[i].get("items_sold"))/len(sells_phone[i].get("items_sold")), 2)
        print(f"По товару - {product} продано - {items_sold} штук. В среднем это {avg_items_sold} штук.")
        all += sum(sells_phone[i].get("items_sold"))
        len_all += len(sells_phone[i].get("items_sold"))
    print(f"Всего продано {all} товаров и в среднем это {round(all/len_all, 2)} штук. ")

if __name__ == "__main__":
    main()
