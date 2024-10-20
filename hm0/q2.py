def two_of_three(i,j,k): 
  return min(i * i + j * j,i * i + k * k,j * j + k * k)



print(two_of_three(10,2,8))