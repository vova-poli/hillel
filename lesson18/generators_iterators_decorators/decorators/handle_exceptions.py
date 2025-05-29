def handle_exceptions(func):
    """Декоратор, який обробляє винятки під час виконання функції."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception caught in {func.__name__}: {e}")
            return None
    return wrapper

@handle_exceptions
def divide(x, y):
    return x / y
