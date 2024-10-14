grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Ср. балл - нашел оптимизацию в виде for... in range(len(...), иначе каждый вручную вписывать... ну это не дело)
#average0 = sum(grades[0]) / len(grades[0])
#average1 = sum(grades[1]) / len(grades[1])
#average2 = sum(grades[2]) / len(grades[2])
#average3 = sum(grades[3]) / len(grades[3])
#average4 = sum(grades[4]) / len(grades[4])
# Множество по алфавиту
students_alf = sorted(students)
# Решение
grades_students = {students_alf[s]: sum(grades[s]) / len(grades[s]) for s in range(len(grades))}
print(grades_students)
