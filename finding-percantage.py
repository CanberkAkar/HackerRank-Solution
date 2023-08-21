n = int(input())
student_records = {}

for _ in range(n):
    name, *marks = input().split()
    marks = list(map(int, marks))
    student_records[name] = marks

query_name = input()

marks = student_records[query_name]
average = sum(marks) / len(marks)

print("{:.2f}".format(average))
