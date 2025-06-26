numbers = [4, -2, 0, 7, -9, 3, -1, 5]

def is_positive(x):
    return x > 0

positive_numbers = list(filter(is_positive, numbers))

print("Musbat sonlar:", positive_numbers)
