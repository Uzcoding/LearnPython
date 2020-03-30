# price = 100
# discount = 20

# price_with_discount = price - price * discount / 100

# print(price_with_discount)

# def discounted(price, discount, max_discount = 50):
#     price = abs(float(price))
#     discount = abs(float(discount))
#     max_discount = abs(float(max_discount))
#     if max_discount > 99:
#         raise ValueError('Максимальная скидка не может быть больше 99%')
#     if discount >= max_discount:
#         price_with_discount = price
#     else:    
#         price_with_discount = price - price * discount / 100
#     return price_with_discount

# # product = { 'name': 'Samsung Galaxt S10', 'stock': 8, 'price': 50000.0, 'discount': 60 }

# # product['with_discount'] = discounted( product['price'], product['discount'], max_discount = 80 )

# # print(product)

# discounted(100, 50, 100)


# Homework

# def get_summ(one, two, delimiter = '&'):
#     return str(one).capitalize() + ' ' + delimiter + ' ' + str(two)

# print( get_summ('learn', 'python') )

# def format_price(price):
#     return 'Цена ' + str( int(price) ) + ' руб.'

# print( format_price(56.24) )