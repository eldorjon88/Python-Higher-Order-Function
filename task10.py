text = ["apple", "34", "banan", "100", "abc", "75"]

numbers = list(filter(lambda x: x.isdigit(), text))

print(numbers)
