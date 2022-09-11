import os

def gradingStudents(grades):
    finalResult = []
    for i in grades:
        if (i+2)%5 == 0 and i >= 38:
            finalResult.append(i+2)
        elif (i+1)%5 == 0 and i >= 38:
            finalResult.append(i+1)
        else:
            finalResult.append(i)
    return finalResult

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
