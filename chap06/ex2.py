#성적이 낮은 순서로 학생 출력하기

"""
    책 답안
    n = int(input())

    array= []
    for i in range(n):
        input_data = input().split()
        array.appen( (input_data[0], input_data[1]) )

    array = sorted(array, key= lambda student: student[1])

    for student in array:
        print(student[0], end=' ') 


"""

n = int(input())

array = []

for i in range(n):
    name, grade = input().split()
    student = (name, int(grade))
    array.append(student)


def settings(data):
    return data[1]

array = sorted(array, key=settings)

for i in array:
    print(i[0], end=' ')