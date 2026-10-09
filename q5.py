# wap to print even length words in a string.
s = input("Enter a string: ")

words = s.split()

for word in words:
    if len(word) % 2 == 0:
        print(word)