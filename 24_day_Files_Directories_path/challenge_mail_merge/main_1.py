#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = '[name]'

# read names and clean data
with open('24_day/challenge_mail_merge/input/names/invited_names.txt') as names_file:
    names = names_file.readlines()
print(names)

with open('24_day/challenge_mail_merge/input/letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, name)
        print(new_letter)
        letter_out_path = f'24_day/challenge_mail_merge/output/ready_to_send/Letter_for_{name}.txt'
        with open(letter_out_path, 'w') as letter_out:
            letter_out.write(new_letter)
    

       




 
    

 



