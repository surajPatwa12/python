#WAP take input from user and print the length of the string
name=(input("enter the name:"))
print("lenght of the name is:" ,len(name))

#conditional statement

age=int(input("enter the age"))
if age >=18:
    print("you are eligible to vote  ,licence , marriage and sex ",age)
elif age<18:
    print("your r not eleggible to vote, licence ,marriage ,sex ",age)
else:
    print("age is not found")
