
def eng_kop_ovoz_toplagan(votes):
    return (max(votes, key=lambda x: x['votes']))

votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]

x = eng_kop_ovoz_toplagan(votes)
print("Eng ko'p ovoz to'plagan", x)
