n = int(input ("enter the number here :"))
if(n>=7 and n<=1):
    print(f"{n} should be the valid number from 1 to 7")
else:
    if(n==1):
        print("Monday")
    elif(n==2):
        print("Tuesday")
    elif(n==3):
        print("Wednesday")
    elif(n==4):
        print("Thursday")
    elif(n==5):
        print("Friday")
    elif(n==6):
        print("Saturday")   
    else: 
        print("Sunday")