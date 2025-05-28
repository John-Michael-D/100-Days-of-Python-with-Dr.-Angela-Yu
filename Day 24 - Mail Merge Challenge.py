#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as docs1:
    recipients = docs1.read().splitlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as docs2:
    contents = docs2.read()
    with open("./Input/Letters/starting_letter.txt", mode="w") as docs3:
        newContent2 = contents.replace("Angela", "Noble 6")
        docs3.write(newContent2)

for i in recipients:
    with open(f"./Output/ReadyToSend/Letter_For_{i}.txt", mode="w") as docs4:
        newContent2 = contents.replace("[name]", f"{i}")
        docs4.write(newContent2)