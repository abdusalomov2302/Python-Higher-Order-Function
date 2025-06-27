
def uzunlik_buyicha_saralash(words):
    words.sort(key=lambda x: len(x))
    return words

words = ["sun", "mountain", "a", "apple"]
x = uzunlik_buyicha_saralash(words)

print("Joyida saralangan:", x)