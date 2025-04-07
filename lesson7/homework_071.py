# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number} x {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(5)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def _sum(a, b):
    return a + b


print(_sum(-6, 35))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def arithmetic_mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


print(arithmetic_mean([5, 6, 0]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reversed_string(input):
    return input[::-1]


print(reversed_string("abcde"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(words):
    if not words:
        return None
    return max(words, key=len)


print(longest_word(['Elephant', 'Cat', 'Fish']))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7


def filter_by_string(lst1):
    lst2 = []
    for x in lst1:
        if type(x) == str:
            lst2.append(x)
    return lst2


print(filter_by_string(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))

# task 8


def sum_of_even(nums):
    return sum(i for i in nums if i % 2 == 0)


print(sum_of_even([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))

# task 9


def title_words_count(text):
    arr_text = text.split(" ")
    title_count = 0

    for i in arr_text:
        if i.istitle():
            title_count += 1
    return title_count

print(title_words_count("Nhhh vmro 2839 Ttt iaaoo L"))

# task 10


def text_with_letter_h():
    while True:
        text = input("Enter your text with letter 'h': ")
        text = text.lower()

        if "h" in text:
            break
        else:
            print("Try again")


text_with_letter_h()

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""