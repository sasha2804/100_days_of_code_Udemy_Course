
# reading first list
with open('26_day/file1.txt','r') as file_1:
    list_1 = file_1.readlines()
list_clean_1 = [int(num) for num in list_1]
print(list_clean_1)

#reading second list
with open('26_day/file2.txt','r') as file_2:
    list_2 = file_2.readlines()
list_clean_2 = [int(num) for num in list_2]
print(list_clean_2)

result = [num for num in list_clean_1 if num in list_clean_2 and num in list_clean_1]

print(result)