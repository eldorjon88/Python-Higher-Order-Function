sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()

top_3 = sorted(words, key=lambda w: len(w), reverse=True)[:3]

print(top_3)
