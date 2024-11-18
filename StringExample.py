#example1
name = "superb" #the word "superb" is stored in (name)

for ch in name: #for every letter in this string
    print(ch,'-',end='') #after every letter insert '-' and it ends with and empty string ''
 
 #example2
 
string1=input("Enter a string :") 
print("The",string1,"in reverse order is:") 
lenght=len(string1)
for a in range(-1,(-lenght-1),-1): #for every letter in this string start at -1 the last letter and go to but not including -8 and -1 to make it arrive to -8.
#And the first -1 means to start from the last letter and go till the first letter last -1 is the stepsise tells you how many steps to skip.
    print(string1[a]) #a is the name given to the input