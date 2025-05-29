from generators.even_numbers import even_numbers
from generators.fibonacci import fibonacci_up_to
from iterators.reverse_list import ReverseList
from iterators.even_iterator import EvenIterator
from decorators.log_args_and_result import add
from decorators.handle_exceptions import divide

print("Генератор парних чисел:")
for n in even_numbers(10):
    print(n, end=" ")
print("\n")

print("Генератор Фібоначчі:")
for f in fibonacci_up_to(21):
    print(f, end=" ")
print("\n")

print("Ітератор зворотного списку:")
for item in ReverseList([1, 2, 3, 4]):
    print(item, end=" ")
print("\n")

print("Ітератор парних чисел:")
for num in EvenIterator(10):
    print(num, end=" ")
print("\n")

print("Декоратор логування:")
add(3, 4)
print()

print("Декоратор обробки винятків:")
print(divide(10, 2))
print(divide(10, 0))
