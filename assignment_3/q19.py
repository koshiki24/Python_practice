print('''
      enter '+' for addition of 2 number : 
      enter '>' for finding the greatest number : 
      enter "==" for finding the numbers are equal or not : ''')
n  = input("enter the symbol here : ")


a = int (input("enter 1st no. : "))
b = int(input("enter 2nd no. : "))

if(n =="+"):
    print(f"print addition of two no. is : {a+b}")
elif (n=='>'):
    print(f"the greatest no. is: {a} ")if a>b else print(f"b is the greatest no. {b}")
elif ( n =="=="):
    print("equal")if a==b else print("not equal")
else:
    print("choose the valid symbol")