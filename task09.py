
def eng_uzun_ism(names):
    return max(names, key = len)

names = ["Ali", "Valijon", "Sami", "Diyorbek"]
result = eng_uzun_ism(names)

print("Eng uzun ism:",result)