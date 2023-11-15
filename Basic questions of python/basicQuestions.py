# Sum of 1 to n terms 

n = 10
sum = 0

for i in range(1, n+1):
    sum += i 

print(f"sum of {n} terms is {sum}")


# Binary search in python 

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid 
        elif mid_element < target:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1  

sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

result = int(binary_search(sorted_array, target_value))

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Value not found in the array")

# Calculate the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(f"The factorial of 5 is {result}")

# Sum of digits of a number 

def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n % 10
        n //= 10

    return digit_sum

number = 34523
result = sum_of_digits(number)
print(f"The sum of digits in {number} is {result}")

# Count the occurrence of each character in a string.

def count_characters(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

string = "hello my name is ram"
char_frequency = count_characters(string)
print(f"Character frequency in '{string}': {char_frequency}")

# Find largest number in a list 

def find_largest_number(lst):
    largest = lst[0] 

    for num in lst[1:]:
        if num > largest:
            largest = num

    return largest
numbers = [12, 5, 27, 8, 15]
result = find_largest_number(numbers)

print(f"The largest number in the list is: {result}")

# Reverse a string in python

def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

original_str = "hello"
reversed_str = reverse_string(original_str)

print(f"Reversed string: {reversed_str}")

# Check if a number is a prime number.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
result = is_prime(11)
print(f"11 is a prime number: {result}")

