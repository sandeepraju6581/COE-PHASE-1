def calculate_result(internal, external, project):
    if internal < 50 or external < 50 or project < 50:
        return "Failed"
    total_score = (internal + external + project) / 3
    if total_score >= 90:
        grade = "A"
    elif 70 <= total_score < 90:
        grade = "B"
    elif 50 <= total_score < 70:
        grade = "C"
    else:
        grade = "Failed"
    return f"Total Score: {total_score:.2f}, Grade: {grade}"
try:
    internal_mark = float(input("Enter the internal marks (out of 100): "))
    external_mark = float(input("Enter the external marks (out of 100): "))
    project_mark = float(input("Enter the project marks (out of 100): "))
    result = calculate_result(internal_mark, external_mark, project_mark)
    print(result)
except ValueError:
    print("Invalid input! Please enter numeric values.")
