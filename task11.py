nums = list(range(1, 21))

juft_kvadratlar = list(
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, nums)
    )
)

print(juft_kvadratlar)
