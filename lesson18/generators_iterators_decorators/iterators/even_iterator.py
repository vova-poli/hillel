class EvenIterator:
    """Ітератор, який повертає парні числа від 0 до n включно."""
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current
        self.current += 2
        return result
