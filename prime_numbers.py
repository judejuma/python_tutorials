def next_prime(num):
    while True:
        num = num + 1
        for i in range (2, num):
            if num%i ==0:
                break
            else:
                return num
def prime_producer(N):
    num =1
    count =1
    while count <=N:
        num = next_prime(num)
        yield num
        count =count + 1
    primes =[ x for x in prime_producer(5)]
    print (primes)