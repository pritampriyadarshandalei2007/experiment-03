# wap to check wheather the string is symmetrical or palinrome.
s = input("Enter a string: ")

n = len(s)

if n % 2 == 0:
    if s[:n//2] == s[n//2:]:
        print("Symmetrical")
    else:
        print("Not Symmetrical")
else:
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")