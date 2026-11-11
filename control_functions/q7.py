'''7. Password Strength Checker
Intermediate
Concepts: Conditions, loops, functions, strings
Requirements
•	Accept a password from the user.
•	Check its length.
•	Check for uppercase and lowercase letters.
•	Check for digits and special characters.
•	Classify it as weak, medium, or strong according to your defined rules.
Bonus: Display suggestions to improve a weak password.
'''
def password():
    password = input("Enter Password :")
    return password

a = password()
upper = 0
lower = 0
digit = 0
sc = 0
count = 0

for ch in a:
    count+=1
    if ord(ch) >= 65 and ord(ch) <= 90:
        upper+=1
    elif ord(ch) >= 97 and ord(ch) <= 122:
        lower+=1
    elif ord(ch) >= 48 and ord(ch) <= 57:
        digit+=1
    else:
        sc+=1
if count >= 8 and upper > 1 and lower > 1 and digit > 1 and sc > 1:
    print("Password is Strong")
elif upper > 0 and lower > 0 and digit > 0 and sc > 0:
    print("Password is medium")
else:
    print("Password is weak")

    if count < 8:
        print("Use atleast 8 characters")
    if upper == 0:
        print("Add uppercase character")
    if lower == 0:
        print("Add lowercase character")
    if digit == 0:
        print("Add digits")
    if sc == 0:
        print("Add special character")
#print(f"Your Password is : {a}")
