num = int(input("enter the number here : "))
if(num<1000 and num>9999):
    print("please enter a four digit number ")
else:
    d4 = num%10
    num = num//10
    
    d3 =num%10
    num = num//10
    
    d2 = num%10
    num = num//10   
    
    d1 = num%10   
    
    print(f"the reversed number is : {d4*1000 + d3*100 + d2*10 + d1}")