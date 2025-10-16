'''
Calculator function
'''

def Add(numbers: str) -> int:
    if not numbers:
        return 0
    
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]
    else:
        delimiter = ","

    numbers = numbers.replace("\n", delimiter)
    list_num = numbers.split(delimiter)
    return sum(int(num) for num in list_num)
