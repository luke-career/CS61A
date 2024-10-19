def divisible_by_k(n,k):
    result = 0
    if(n < k):
       return 0
    num = 1
    while(num <= n):
      if(num % k == 0):
         result +=1
      num +=1
    return result

print(divisible_by_k(3,1))
  