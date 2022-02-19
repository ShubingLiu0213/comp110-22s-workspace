"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730508266"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters.")    
    exit()
one: str = input("Enter a single character: ")
if len(one) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + one + " in " + word)
if word[0] == one:
    print(one + " found at index 0")
if word[1] == one:
    print(one + " found at index 1")
if word[2] == one:
    print(one + " found at index 2")
if word[3] == one:
    print(one + " found at index 3")
if word[4] == one:
    print(one + " found at index 4")
count: int = 0
if word[0] == one:
    count = count + 1
if word[1] == one:
    count = count + 1
if word[2] == one:
    count = count + 1    
if word[3] == one:
    count = count + 1      
if word[4] == one:
    count = count + 1
if count == 1:
    print(str(count) + " instance of " + one + " found in " + word)
else:
    if count == 0:
        print("No instances of " + one + " found in " + word)
    else:
        print(str(count) + " instances of " + one + " found in " + word)


           

 
 
