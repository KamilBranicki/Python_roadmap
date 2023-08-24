students_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

for (key, value) in students_dict.items():
    print(value)

import pandas

students_data = pandas.DataFrame(students_dict)
print(students_data)

# Loop through  a data frame
# for (key, value) in students_data.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in students_data.iterrows():
    if row.student == "Angela":
        print(row.score)