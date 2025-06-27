

def a(numbers):
    return list(filter(lambda a: a > 0,numbers))

numbers = [4, -2, 0, 7, -9, 3, -1, 5]

positive_numbers = a(numbers)

print(positive_numbers)
