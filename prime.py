def is_prime(number):
    if number == 1:
        return False
    for factor in range (2, number):
        if number % 2 ==0:
            return False
        return True
def print_primes (n):
    for number in range (1,n+1):
        if is_prime(number):
            print ('%d is prime' % number)
print_primes(50)

dir('name')