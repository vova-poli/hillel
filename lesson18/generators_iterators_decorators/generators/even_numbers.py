def even_numbers(n):
    """Генератор, який повертає парні числа від 0 до n включно."""
    for i in range(0, n + 1, 2):
        yield i
