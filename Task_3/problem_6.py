def analyze_grades(grades):
    if len(grades) == 0:
        return "List is empty"

    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    return {
        "average": average,
        "highest": highest,
        "lowest": lowest
    }

print(analyze_grades([60, 70, 80]))
print(analyze_grades([100]))
print(analyze_grades([]))