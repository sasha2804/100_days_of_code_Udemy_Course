#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#letter_path = 'E:/Python/git_Udemy_100_days_of_code/100_days_of_code_Udemy_Course/100_days_of_code_Udemy_Course/24_day/challenge_mail_merge/input/letters/starting_letter.txt'
from heapq import nsmallest
from unicodedata import name


letter_path = '24_day/challenge_mail_merge/input/letters/starting_letter.txt' # path to read input
names_path = '24_day/challenge_mail_merge/input/names/invited_names.txt' # path to read input


# read letters
letter = open(letter_path,'r')
letter_in = letter.readlines()
print(letter_in)

# read names
names = open(names_path, 'r')
names_in = names.readlines()
print(names_in)

#replace names in letters
txt = letter_in[0]
txt_adapt = txt.replace('[name]', 'new_name')
# strip names



for name in names_in:    
    letter_in[0] = txt.replace('[name]', name)
    print(letter_in)
    letter_out_path = f'24_day/challenge_mail_merge/output/ready_to_send/Letter_for_{name}.txt'
    with open(letter_out_path, 'w') as data:
        data.write(str(letter_in)) # path to write output




# letter_name = 'Cook'
# letter_out_path = f'24_day/challenge_mail_merge/output/ready_to_send/Letter_for_{letter_name}.txt'


# with open(letter_out_path, 'w') as data:
#     data.write(str(letter_in).strip()) # path to write output


# for i in names_in:
#     print(i)



# write lettes as separate files

# letter_in[0] = txt_adapt
# print(letter_in)

# letter_name = 'Cook'
# letter_out_path = f'24_day/challenge_mail_merge/output/ready_to_send/Letter_for_{letter_name}.txt'


# with open(letter_out_path, 'w') as data:
#     data.write(str(letter_in).strip()) # path to write output



