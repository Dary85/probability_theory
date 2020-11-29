from math import sqrt
salary = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

#среднее арифметическое
avg = sum(salary)/len(salary)
print(f"среднее арифметическое: {avg}")

#среднее квадратичное отклонение

print(f"среднее арифметическое: {sqrt(sum((i-avg)**2 for i in salary)/len(salary))}")

#смещенную и несмещенную оценки дисперсий для данной выборки.

print(f"смещенная дисперсия: {sum((i-avg)**2 for i in salary)/len(salary)}")
print(f"несмещенная дисперсия: {sum((i-avg)**2 for i in salary)/(len(salary)-1)}")