grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

stud = list(students)
students_ = sorted(stud)
print('Студенты по алфавиту:', students_)

grades_ = []

sum_0 = sum(grades[0]) 
len_0 = len(grades[0])
score_0 = sum_0 / len_0
grades_.append(float(score_0))

sum_1 = sum(grades[1]) 
len_1 = len(grades[1])
score_1 = sum_1 / len_1
grades_.append(float(score_1))

sum_2 = sum(grades[2]) 
len_2 = len(grades[2])
score_2 = sum_2 / len_2
grades_.append(float(score_2))

sum_3 = sum(grades[3]) 
len_3 = len(grades[3])
score_3 = sum_3 / len_3
grades_.append(float(score_3))

sum_4 = sum(grades[4]) 
len_4 = len(grades[4])
score_4 = sum_4 / len_4
grades_.append(float(score_4))

print('Среднее значение оценок:', grades_)

dict_ = {}

dict_[students_[0]] = score_0
dict_[students_[1]] = score_1
dict_[students_[2]] = score_2
dict_[students_[3]] = score_3
dict_[students_[4]] = score_4

print('Оценки студентов:', dict_)
