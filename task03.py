

def a(numbers):
    if not numbers:
        return None, None
    return max(numbers) , min(numbers)


numbers = [18, 29, 3, 45, 7, 12]

eng_katta, eng_kichina = a(numbers)

print("Eng kattasi: ", eng_katta)
print("Eng kichkina: ", eng_kichina)
