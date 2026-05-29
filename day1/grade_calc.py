exp1 = float(input())
exp2 = float(input())
exp3 = float(input())

avg = (exp1 + exp2 + exp3)/3

if avg > 90:
    grade = "A"
elif avg > 80:
    grade = "B"
elif avg > 70:
    grade = "C"
else:
    grade = "D"

print('Average: ', avg)
print('Grade: ', grade)