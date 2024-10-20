def largest_factor(n):
  max = 1
  temp = 1
  while temp < n:
    if n % temp == 0 :
       max = temp
    temp += 1
  return max

print(largest_factor(13))