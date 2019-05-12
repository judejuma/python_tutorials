def even_numbers(num):
    if num < 10:
        print("The prime numbers are less then 5")
    numbers =[]
    count = 0
    for i in range(2, num):
        if i % 2 == 0:
            numbers.append(i)
            count = count +1
        if count == 5:
            break

    print(numbers)
even_numbers(5)