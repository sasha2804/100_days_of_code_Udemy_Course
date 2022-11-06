import random
import pandas as pd

# names = ['Alex', 'Angela', 'Caroline', 'Tom']
# students_scores = {student:random.randint(1, 10) for student in names}
# print(students_scores)
# passed_students = {student:score for (student, score) in students_scores.items() if score > 2}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)

student_dict = {
    'students': ['Alex', 'Angela', 'Caroline', 'Tom'],
    'score': [12,15,20,50]
}
df = pd.DataFrame(student_dict)
for (index,row) in df.iterrows():
    print(row.students, row.score)
    # if row.students == 'Alex':
    #     print(row.score)


