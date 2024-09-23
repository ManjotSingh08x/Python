number = int(input("Enter a number: "))

if number % 6 == 0:
    print("It is divisible by 2 and 3")
elif number % 3 == 0:
    print("It is divisible by 3 only")
elif number % 2 == 0:
    print("It is divisble by 2 only ")
else:
    print("It is not divisible by either 2 or 3")
