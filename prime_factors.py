#10 2,5
#20 2,5
def prime_factors(num):
  factors = []
  factor = 2
  while (num >= 2):
    if (num % factor == 0): #42%2 remainder is 0
      factors.append(factor) #add 2 in the list
      num = num / factor # new num is 42/2 which is 21
    else:
      factor += 1
  return factors

prime_factors(12) # [2,2,3]
prime_factors(42) # [2,3,7]

#24,24/2=12,12/2=6,6/2=3