def sum_of_numbers_in_string(list_of_nums):
    try:
        numbers = list(map(int, list_of_nums.split(",")))
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити"

list_of_nums = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in list_of_nums:
    result = sum_of_numbers_in_string(item)
    print(result)
