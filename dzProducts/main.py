"""
ЗАДАНИЕ 1 (Обязательно)

1.	написать код для https://github.com/makarova1507ana/python323/tree/main/%D0%9E%D0%9E%D0%9F/%D0%BA%D0%BE%D1%80%D0%B7%D0%B8%D0%BD%D0%B0%20%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2 
1.1.	Запрещено менять:
1.1.1.	list_products , атрибуты класса (должны остаться закрытыми )
1.2.	необходимо реализовать возможность подсчета стоимости товаров в корзине

"""

from Product import Product


def append_to_shop_cart():
    # цикл для добавления товаров пользователем
    while True:
        # номер товара опеделяет пользователь
        user_choice = input(
            'would you like the product of number ... ')  # дописать условия добавления и т.д. выход из системы
        if user_choice == '0':
            break

        # добавит блок проверки перед добавлением в корзину попапку
        shop_cart.append(list_products[int(user_choice) - 1])


def show_shop_cart():
    i = 1
    print('\n ***************shop_cart***************')
    for product in shop_cart:
        print(str(i) + ". ", end='')
        product.show()
        i += 1


# список всех товаров в магазине
list_products = [Product('short', 'одежда', 250), Product('boots', 'обувь', 2000), Product('jerry', 'украшение', 10000)]

i = 1
shop_cart = []
for product in list_products:
    print(str(i) + ". ", end='')
    product.show()
    i += 1

append_to_shop_cart()

# список добавленных товаров в корзину
show_shop_cart()

to_pay = 0

for product in shop_cart:
    to_pay += product.cost

print(f'К оплате: {to_pay}')







# через класс магазин
# Создать класс Корзина товаров ->
# Для данного задания понадобится класс товар (название, тип(одежда, обувь, украшение), стоимость)
# реализовать общий список всех товаров
# список добавленных товаров в корзину
# необходимо реализовать возможность подсчета товаров

# from Product import *
# from Shop import *
# from ShopCart import *
#
# shop = Shop('SHOP_2_0', Product('short', 'одежда', 250), Product('boots', 'обувь', 2000),
#             Product('jerry', 'украшение', 10000))
# shop.show()
#
# shop_cart = ShopCart()
# while True:
#     # номер товара опеделяет пользователь
#     user_choice = input(
#         'would you like the product of number ... ')  # дописать условия добавления и т.д. выход из системы
#     if user_choice == '0':
#         break
#     # добавит блок проверки перед добавлением в корзину попапку
#     product = shop.products[int(user_choice) - 1]
#
#     shop_cart.append_product(product)
#
# shop_cart.show()
# print(shop_cart.cost_products)
