#Message
print("*** Welcome to Student Information ***")

#Input
student_name = input("Enter student Name: ")
student_id = int(input("Student Id: "))
sub1_marks = int(input("Sub1 marks: "))
sub2_marks = int(input("Sub2 marks: "))
sub3_marks = int(input("Sub3 marks: "))
sub4_marks = int(input("Sub4 marks: "))
sub5_marks = int(input("Sub5 marks: "))
sub6_marks = int(input("Sub6 marks: "))


#total marks
total_marks = sub1_marks + sub2_marks + sub3_marks + sub4_marks + sub5_marks + sub6_marks


#percentage
percentage = (total_marks / 360) * 100


#grade
if total_marks >= 301:
    grade = "A"
elif total_marks >= 201:
    grade = "B"
elif total_marks >= 101:
    grade = "C"
else:
    grade = "D"


#result
if sub1_marks >= 35 and sub2_marks >= 35 and sub3_marks >= 35 and sub4_marks >= 35 and sub5_marks >= 35 and sub6_marks >= 35:
    result = "PASS"
else:
    result = "FAIL"


#Output
print("\nStudent name:", student_name)
print("Student Id:", student_id)
print("Total marks:", total_marks)
print("Percentage: {:.2f}%".format(percentage))
print("Student grade:", grade)
print("Result:", result)