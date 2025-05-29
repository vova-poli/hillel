def fibonacci_up_to(n):
    """Генератор послідовності Фібоначчі до n включно."""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
