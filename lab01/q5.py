def sum_digits(y):
  result = 0
  while(y != 0):
    result += (y % 10)
    y = y // 10
  return result

print(sum_digits(4))