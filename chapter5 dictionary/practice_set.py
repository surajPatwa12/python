#1/Write a program to input eight numbers from the user and display all the unique  numbers (once).
a=set()
for a in range(0,8):
    print(a)

#2/Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
a={
     "नमस्ते": "Hello",
     "धन्यवाद": "Thank you",         
    "शुभकामनाएँ": "Best wishes",
     "सुप्रभात": "Good morning",
}
word=input("enter the word")
print(a[word])


#3/ What will be the length of following set S:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations? # This will return the number of unique elements in the set
print(len(s))

#4/ Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
s={}
name=(input("enter your name "))
lang=(input("enter your lang "))
s.update({name:lang}) 

name=(input("enter your name "))
lang=(input("enter your lang "))
s.update({name:lang}) 

name=(input("enter your name "))
lang=(input("enter your lang "))
s.update({name:lang}) 

name=(input("enter your name "))
lang=(input("enter your lang "))
s.update({name:lang}) 

print(s)


