def filter_by_string(lst1: list) -> list:
    lst2 = []
    for x in lst1:
        if type(x) == str:
            lst2.append(x)
    return lst2


def sum_of_even(nums: list) -> int:
    return sum(i for i in nums if i % 2 == 0)


def arithmetic_mean(numbers: list) -> float:
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)