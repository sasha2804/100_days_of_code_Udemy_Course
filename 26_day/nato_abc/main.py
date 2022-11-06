# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd
data = pd.read_csv('26_day/nato_abc/nato_phonetic_alphabet.csv')
print(data)
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Enter word: ').upper()
phon_code = [nato_dict[i] for i in user_input]
print('Get your phonetic words list: ',phon_code)




# passed_students = {student:score for (student, score) in students_scores.items() if score > 2}

