name=input("your name\n")
age=input("your age\n")
phone=input("your phone\n")

if(int(age)>18 and age.isdigit()):
    print("correct age")
if(len(phone)==10 and phone.isdigit()):
    print("correct phone")
else:
    print("enter correct age and phone")