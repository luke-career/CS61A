def falling(n,k):
  if k == 0:
     result = 1
  result = 1
  for i in range(k):
      result *= n - i
  print(result)
   


