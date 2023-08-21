if __name__ == '__main__':
    n = int(input())
    students = []
    
    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])
    
    # Find the second lowest grade
    grades = list(set([student[1] for student in students]))
    grades.sort()
    second_lowest_grade = grades[1]
    
    # Find the students with the second lowest grade
    second_lowest_students = []
    for student in students:
        if student[1] == second_lowest_grade:
            second_lowest_students.append(student[0])
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print each student's name on a new line
    for student in second_lowest_students:
        print(student)