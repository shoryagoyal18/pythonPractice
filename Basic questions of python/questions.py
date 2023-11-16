# Remove Duplicates from a List

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Unique Numbers:", unique_numbers)

# Reverse a List using a Loop

numbers = [1, 2, 3, 4, 5]
reversed_numbers = []
for i in range(len(numbers) - 1, -1, -1):
    reversed_numbers.append(numbers[i])
print("Reversed List:", reversed_numbers)

# Loop through a string and count vowels.

word = "This is a python code"
vowel_count = 0
for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowel_count += 1
print("Vowel Count:", vowel_count)

# Print first 10 terms in fibonacci series 

a = 0 
b = 1
for _ in range(10): 
    c = a+b
    print(c, end=" ")
    a = b
    b = c

# Find the largest common divisor (GCD) of two numbers.

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

num1, num2 = 24, 36
gcd = find_gcd(num1, num2)
print("GCD:", gcd)
