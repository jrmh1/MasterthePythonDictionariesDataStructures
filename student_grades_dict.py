student_grades = {
    'Student1': 'B',
    'Student2': 'C',
    'Student3': 'A',
    'Student4': 'B+',
    'Student5': 'A-'
}

print("Entire dictionary:", student_grades)

print("Grade of third student:", student_grades['Student3'])

student_grades['Student2'] = 'A'
print("Updated dictionary after modifying Student2's grade:", student_grades)

del student_grades['Student5']
print("Dictionary after deleting Student5:", student_grades)

last_key = list(student_grades.keys())[-1]
last_value = student_grades[last_key]
print(f"Last key-value pair: {last_key}: {last_value}")
