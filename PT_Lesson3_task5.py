# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
# для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:
# а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
p1 = 0.1
p2 = 0.2
p3 = 0.25
q1 = 1-p1
q2 = 1-p2
q3 = 1-p3

print(f"все детали: {p1*p2*p3}")
print(f"только две детали: {p1*p2*q3+p1*q2*p3+q1*p2*p3}")
print(f"хотя бы одна деталь: {(p1*p2*q3+p1*q2*p3+q1*p2*p3)+(p1*p2*p3)+(p1*q2*q3+q1*p2*p3+p1*p2*q3)}")
print(f"от одной до двух деталей: {(p1*p2*q3+p1*q2*p3+q1*p2*p3)+(p1*q2*q3+q1*p2*p3+p1*p2*q3)}")