print("Enter the input string, the program willo give the first 2 and the last2 characters, if the string is shorter, it will produce an empty string")
string=input()
lenght=len(string)
if int(lenght) < 4:
    print("Empty string") #loooooooooooooooooool
else:
    print(string[0]+string[1]+string[lenght-2]+string[lenght-1])
