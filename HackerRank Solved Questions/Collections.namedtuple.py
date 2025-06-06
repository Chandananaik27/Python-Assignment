from collections import namedtuple
student_no=int(input())
columns=input().split()
student=namedtuple("student",columns)
info_student=[student(*input().split()) for _ in range (student_no)]
avg=sum(int(student.marks) for student in info_student)/student_no
print(avg)