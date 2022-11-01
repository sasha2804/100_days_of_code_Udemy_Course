#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# read names and clean data
with open('24_day/challenge_mail_merge/input/names/invited_names.txt', 'r') as names:
    names.readlines()

print(names)

# names = open(names_path, 'r')
# names_in = names.readlines()
# for name in names_in:
#     name_temp.append(name.strip())
# names_in = name_temp.copy()
# name_temp.clear()

# letter_path = '24_day/challenge_mail_merge/input/letters/starting_letter.txt' # path to read input
# names_path = '24_day/challenge_mail_merge/input/names/invited_names.txt' # path to read input

# letter_temp = [] # temporary list
# name_temp = [] # temporary list

# # read letters and clean data
# letter = open(letter_path,'r')
# letter_in = letter.readlines()
# for str in letter_in:
#     if str.strip() != '':
#         letter_temp.append(str.strip())
# letter_in = letter_temp.copy()
# letter_temp.clear()    

# # read names and clean data
# names = open(names_path, 'r')
# names_in = names.readlines()
# for name in names_in:
#     name_temp.append(name.strip())
# names_in = name_temp.copy()
# name_temp.clear()

# # replace name and write letter as separate files
# for name in names_in:
#     letter_out = letter_in.copy() 
#     letter_out[0] = letter_in[0].replace('[name]', name)
#     letter_out_path = f'24_day/challenge_mail_merge/output/ready_to_send/Letter_for_{name.strip()}.txt'
#     with open(letter_out_path, 'w') as data:
#             for i in letter_out:
#                 data.write(i+'\n\n')
    

    
 
    

 



