#Example1: string.capitalize()
#Returns a copy of the string with its first character capitalized.

"true".capitalize() #Turns the string "true" in capital, turning it in "True".
"i love my India.".capitalize() #The same thing.

#Example2: string.find(sub[, start[, end]])
#Returns the lowest index in the string where the substring sub is found within the slice range of start and end. Returns 1 if sub is not found.

string = "it goes as - ringa ringa roses" 
sub = "ringa"
a  = string.find(sub) #the string looks for sub which is "ringa", and is stored in a.
print(a) #prints at what position "ringa" begins.
b = string.find(sub, 15, 25)
print(b)
c = string.find(sub, 15, 22)
print(c)
d = string.find(sub, 15)
print(d)
"string".isalnum()

#Example3: string.isalnum()
#Note: ie. a = string is not needed for the program to work, but it is used for convinience.
a = string = "abc123"
print(a)
b = string2 = 'hello'
print(b)
c = string3 = '12345'
print(c)
d = string4 = ' '
print(d)

#Checks if the characters in the string are alphanumeric, if they are it's true if not false
a = string.isalnum() 
print(a)
b = string2.isalnum()
print(b)
c = string3.isalnum()
print(c)
d = string4.isalnum()
print(d)

#Example4: string.alpha()
#Checks if the characters in the string are alphabetic, if they are it's true if not false
print("Example4:")
a = string.isalpha() 
print(a)
b = string2.isalpha()
print(b)
c = string3.isalpha()
print(c)
d = string4.isalpha()
print(d)

#Example5: string.isdigit()
#Checks if the characters in the string are digits, if they are it's true if not false.
print("Example5:")
a = string.isdigit()
print(a)
b = string2.isdigit()
print(b)
c = string3.isdigit()
print(c)
d = string4.isdigit()
print(d)

#Example6: string.islower()
#Checks if the characters in the string are lowercase, if they are it's true if not false.
print("Example6:")
a = string = 'hello'
print(a)
b = string2 = 'THERE'
print(b)
c = string3 = 'Goldy'
print(c)
a = string.islower()
print(a)
b = string2.islower()
print(b)
c = string3.islower()
print(c)






