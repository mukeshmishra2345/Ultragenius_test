'''Method take input as number to get numbers as output'''

def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers = numbers.replace("\n", ",")
    number_list = numbers.split(",")
    number_list = [int(num) for num in number_list if num]

    return sum(number_list)
