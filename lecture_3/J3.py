def lang(languages: list) -> tuple:
    com = languages[0]
    ind = languages[0]
    for language in range(1, len(languages)):
        com = com.intersection(languages[language])
        ind = ind.union(languages[language])
    return len(com), com, len(ind), ind


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        f = reader.read().rstrip().split('\n')
    n, students = int(f[0]), f[1:]
    languages_, student_number = [], 0
    while student_number < len(students):
        current_student = int(students[student_number])
        languages_.append(set(students[student_number + 1:student_number + current_student + 1]))
        student_number += current_student + 1

    result = lang(languages_)
    print(result[0])
    for i in result[1]:
        print(i)
    print(result[2])
    for i in result[3]:
        print(i)
