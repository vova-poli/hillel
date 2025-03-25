import math

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area_size = 436402
azov_sea_area_size = 37800
print(f"Total area is {black_sea_area_size + azov_sea_area_size}")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
goods_total = 375291
first_depot_amount = goods_total - 222950  # віднімаємо від загальної кількості суму 2 і 3 складів
third_depot_amount = goods_total - 250449  # віднімаємо від загальної кількості суму 1 і 2 складів
second_depot_amount = goods_total - first_depot_amount - third_depot_amount
print(f"first depot = {first_depot_amount}, second depot = {second_depot_amount}, third depot = {third_depot_amount}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
months_amount = 18
monthly_payment = 1179
print(f"Total price is {months_amount * monthly_payment}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f"8019 % 8 = {8019 % 8}")
print(f"9907 % 9 = {9907 % 9}")
print(f"2789 % 5 = {2789 % 5}")
print(f"7248 % 6 = {7248 % 6}")
print(f"7128 % 5 = {7128 % 5}")
print(f"19224 % 9 = {19224 % 9}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_large = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
print(f"Order total is {pizza_large + pizza_medium + juice + cake + water}")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_amount = 232
page_limit = 8
page_amount = math.ceil(photo_amount / page_limit)  # math.ceil() у разі, якщо результатом ділення кількості фото на ліміт фотографій буде не ціле число
print(f"Total pages: {page_amount}")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
petrol_consumption_per_100km = 9
tank_capacity = 48
total_petrol_needed = (distance / 100) * petrol_consumption_per_100km
refill_count = math.ceil(total_petrol_needed / tank_capacity)  # Округлення до цілого числа (бо заїхати на заправку доведеться цілу кількість разів)
print(f"Total petrol needed: {total_petrol_needed}")
print(f"Refills needed: {refill_count}")
