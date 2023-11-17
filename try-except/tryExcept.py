try:
  num1 = 10
  num2 = 0
  result = num1 / num2
  print(result)
except ZeroDivisionError:
  print("Error: Cannot divide by zero.")
except ValueError:
  print("Error: Invalid input.")