purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
min_price = 1 # минимальная цена
# item — название товара,
# category — категория товара,
# price — цена за единицу товара,
# quantity — количество единиц, купленных за один раз.

def total_revenue(purchases): # Рассчитайте и верните общую выручку (цена * количество для всех записей).
    return sum(map(lambda x: x['price']*x['quantity'], purchases))


def items_by_category(purchases): # Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
    d = {}
    for i in purchases:
        d.setdefault(i['category'], []).append(i['item'])
    return d


def expensive_purchases(purchases, min_price): # Выведите все покупки, где цена товара больше или равна min_price.
    return list(filter(lambda x: x['price']>=min_price, purchases))


def average_price_by_category(purchases): # Рассчитайте среднюю цену товаров по каждой категории.
    d = dict.fromkeys(map(lambda x: x['category'], purchases), 0)
    for k in d:
        l = list(map(lambda x: x['price'], filter(lambda x: x['category']==k, purchases)))
        d[k] = sum(l) / len(l)
    return d


def most_frequent_category(purchases): # Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
    d = dict.fromkeys(map(lambda x: x['category'], purchases), 0)
    for k in d:
        d[k] = sum(map(lambda x: x['quantity'],filter(lambda x: x['category']==k,purchases)))
    return max(d,key = lambda x: d[x])

print(f'''Общая выручка: {total_revenue(purchases)}
Товары по категориям: {items_by_category(purchases)}
Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}
Средняя цена по категориям: {average_price_by_category(purchases)}
Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}''')