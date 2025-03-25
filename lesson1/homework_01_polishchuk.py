# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
first_side = 1
second_side = 2
third_side = 3
fourth_side = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = first_side + second_side + third_side + fourth_side
print(perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_tree_amount = 4
pear_tree_amount = apple_tree_amount + 5
plum_tree_amount = apple_tree_amount - 2
print(apple_tree_amount + pear_tree_amount + plum_tree_amount)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
zero_temperature = 0
before_dinner_temperature = zero_temperature + 5
after_dinner_temperature = before_dinner_temperature - 10
evening_temperature = after_dinner_temperature + 4
print(evening_temperature)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скільки сьогодні дітей у театральному гуртку?
"""
boys_amount = 24
girls_amount = 24 // 2
overall_theater_group_size = boys_amount + girls_amount
today_theater_group_size = overall_theater_group_size - 1 - 2
print(today_theater_group_size)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price) / 2
all_books_price = first_book_price + second_book_price + third_book_price
print(all_books_price)