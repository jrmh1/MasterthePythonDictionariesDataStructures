university_courses_dict = {
    'University of the Philippines': 'Medicine',
    'Ateneo de Manila University': 'Business Management',
    'De La Salle University': 'Engineering',
    'University of Santo Tomas': 'Law',
    'Mapúa University': 'Architecture',
    'Far Eastern University': 'Nursing',
    'Polytechnic University of the Philippines': 'Accountancy',
    'University of San Carlos': 'Education'
}

print("Entire dictionary:", university_courses_dict)

third_university_course = list(university_courses_dict.items())[2]
print("Course of the 3rd university:", third_university_course)

university_courses_dict['Mapúa University'] = 'Information Technology'

del university_courses_dict['Polytechnic University of the Philippines']

last_university_course = list(university_courses_dict.items())[-1]
print("Last key-value pair:", last_university_course)
