

def saralash(emails):
    return emails.endswith('@gmail.com')

emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
x = list(filter(saralash,emails))

print(x)