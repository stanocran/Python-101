#Program to print prime numbers between 1 and 250
 
for possiblePrime in range(2, 251):
    
    # Assume number is prime until shown it is not. 
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
      
    if isPrime:
        print(possiblePrime)