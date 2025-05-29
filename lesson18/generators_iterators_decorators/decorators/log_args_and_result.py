def log_args_and_result(func):
    """Декоратор, який логує аргументи та результат функції."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_args_and_result
def add(x, y):
    return x + y
