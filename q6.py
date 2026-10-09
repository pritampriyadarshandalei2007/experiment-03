# wap to remove all duplicares from a given string.
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch not in result:
        result = result + ch

print("After removing duplicates:", result)