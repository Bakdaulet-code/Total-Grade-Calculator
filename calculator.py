def calculate_final_grade(midterm_grade, endterm_grade):
    total_grade = midterm_grade * 0.3 + endterm_grade * 0.3
    final_grade = (90 - total_grade) / 0.4
    return final_grade

def calculate_total_grade(midterm_grade, endterm_grade, final_exam_grade):
    total_grade = midterm_grade * 0.3 + endterm_grade * 0.3 + final_exam_grade * 0.4
    return total_grade

midterm_grade = float(input("Enter your midterm grade: "))
endterm_grade = float(input("Enter your endterm grade: "))
final_grade = calculate_final_grade(midterm_grade, endterm_grade)

if final_grade < 0:
    print("Congratulations, you already have a total grade of 90% or higher.")
else:
    print("You need to get at least a", final_grade, "% on your final exam to have a total grade of 90% or higher.")
    total_grade = calculate_total_grade(midterm_grade, endterm_grade, 100)
    print("If you score 100% on the final exam, your total grade will be", total_grade, "%.")
