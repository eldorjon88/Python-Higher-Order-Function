prices = ["$120", "$340", "$50", "$90"]

numbers = list(map(lambda price: price.replace("$", ""), prices))

print(numbers)
