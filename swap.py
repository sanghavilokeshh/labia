def swap_numbers_temp(a, b):
  """Swaps two numbers using a temporary variable."""
  temp = a
  a = b
  b = temp
  return a, b

# Example usage:
num1 = 15
num2 = 25

num1, num2 = swap_numbers_temp(num1, num2)

print(f"After swapping, num1 is: {num1}")  # Output: After swapping, num1 is: 25
print(f"After swapping, num2 is: {num2}")  # Output: After swapping, num2 is: 15
