age = int (input("Enter the age here : "))

sex = input('Enter M for male and F for female here : ')
status = input('Enter Y for married and N for unmarried here : ')
if age < 20 or age > 60:
    print("ERROR")
elif sex == 'F'or sex =='f':
    print("Place of service: Urban areas only")
elif sex == 'M'or sex =='m':
    if age<=40 and age>=20:
        print("Place of service: Anywhere")
    elif age>40 and age<=60:
        print("Place of service: Urban areas only")
else:
    print("ERROR")