def evaluate_scholarship(student_name, percentage_10, percentage_12, percentage_ug, family_income):
    if percentage_10 >= 85 and percentage_12 >= 85 and percentage_ug >= 85 and family_income < 3:
        return f"{student_name} is eligible for a Full Scholarship."
    elif percentage_ug >= 70 and family_income < 5:
        return f"{student_name} is eligible for a Partial Scholarship."
    else:
        return f"{student_name} is not eligible for a scholarship."

student_name = input("Enter student name: ")
percentage_10 = float(input("Enter % in 10th: "))
percentage_12 = float(input("Enter % in 12th: "))
percentage_ug = float(input("Enter % in UG: "))
family_income = float(input("Enter family income (in LPA): "))

result = evaluate_scholarship(student_name, percentage_10, percentage_12, percentage_ug, family_income)
print(result)
