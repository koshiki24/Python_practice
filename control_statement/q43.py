n = int(input("Enter binary number :"))
decimal = 0
power = 1
while n > 0:
    a = n%10
    decimal = decimal+a*power
    power = power*2
    n = n//10
print(f"Decimal is : {decimal}")