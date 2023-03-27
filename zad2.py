def czy_pierwsza(*numbers):
    for num in numbers:

        dzielniki = 0

        for i in range(1,num+1):
            if num%i == 0:
                dzielniki += 1

        if dzielniki == 2:
            print(f"{num} is prime")
        else:
            print(f"{num} is not prime")