#STRING MANIPULATION: CHAPTER 9: Pag.287
#5. Write a program that takes a string with multiple words and then capitalizes the first letter of each word and forms a new string out of it.
string = input("Enter a string: ") 
length = len(string) #(lenght) = the lenght of (string)
result = "" #
a = 0
while a < length:
    if a == 0:  
        result += string[a].upper()
        a += 1
    elif string[a] == " " and a + 1 < length and string[a + 1] != " ": 
        result += string[a]  
        result += string[a + 1].upper() 
        a += 2  
    else:
        result += string[a]
        a += 1
print("Original String:", string)
print("Capitalized Words String:", result)

#6. Write a program that reads a string and checks whether it is a palidrome string or not. (Example, noon and racecar are the same either way)

string = input("Enter a string: ")
length = len(string)
mid = lenght // 2 
rev = -1

