def grading_students(grades):
    # Write your code here
    L = []
    for grade in grades:
        if grade >= 38 and grade % 5 != 0:
            rem = grade % 5
            mult_five = grade + (5 - rem)
            if mult_five - grade < 3:
                grade = mult_five
                L.append(grade)
            else:
                L.append(grade)

        else:
            L.append(grade)

    return L


if __name__ == '__main__':
    grades = [34, 29, 57, 68, 73]
    print(grading_students(grades))
