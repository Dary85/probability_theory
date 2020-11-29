# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. Из первого
# ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
from math import factorial


def combination(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


# два белых из 8 мячей +1 белый из второго ящика
p1 = combination(5, 2) / combination(8, 2)  # два белых из 8 мячей
p2 = combination(5, 1)*combination(7,3) / combination(12, 4)  # 1 белый из второго ящика
p11 = p1 * p2
print(p1, p2, p11)

# один белый из 8 мячей +2 белых из второго ящика
p1 = combination(5, 1)*combination(3,1)/ combination(8, 2)  # один белый из 8 мячей
p2 = combination(5, 2)*combination(7,2) / combination(12, 4)  # 1 белый из второго ящика
p22 = p1 * p2
print(p1, p2, p22)

# ноль белый из 8 мячей +3 белых из второго ящика
p1 = combination(5, 0) *combination(3,2)/ combination(8, 2)  # ноль белых из 8 мячей
p2 = combination(5, 3) *combination(7,1)/ combination(12, 4)  # 1 белый из второго ящика
p33 = p1 * p2
print(p1, p2, p33)

# Какова вероятность того, что 3 мяча белые?
print(f"3 мяча белые: {p11 + p22 + p33}")
