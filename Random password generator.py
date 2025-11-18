import random
import string

print("Choose Password Type:")
print("1. Only Letters")
print("2. Only Numbers")
print("3. Letters + Numbers")
print("4. Strong Password (Letters + Numbers + Symbols)")

choice = int(input("Enter your choice (1-4): "))
length = int(input("Enter password length: "))

# character sets
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# selecting character set based on user choice
if choice == 1:
    chars = letters
elif choice == 2:
    chars = numbers
elif choice == 3:
    chars = letters + numbers
elif choice == 4:
    chars = letters + numbers + symbols
else:
    print("Invalid choice!")
    exit()

# generating password
password = "".join(random.choice(chars) for _ in range(length))

print("\nGenerated Password:", password)