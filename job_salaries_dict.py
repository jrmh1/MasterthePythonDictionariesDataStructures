job_salaries_dict = {
    'Software Engineer': 95000,
    'Data Scientist': 105000,
    'Product Manager': 120000,
    'Web Developer': 85000,
    'Graphic Designer': 55000,
    'Marketing Manager': 80000,
    'UX/UI Designer': 75000,
    'Project Manager': 95000,
    'Sales Executive': 60000,
    'Business Analyst': 70000
}

print("Entire dictionary:", job_salaries_dict)

third_job_salary = list(job_salaries_dict.items())[2]
print("Salary of the 3rd job:", third_job_salary)

job_salaries_dict['UX/UI Designer'] = 80000

del job_salaries_dict['Sales Executive']

last_job_salary = list(job_salaries_dict.items())[-1]
print("Last key-value pair:", last_job_salary)
