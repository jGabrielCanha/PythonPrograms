eq1 = input("digite a equação da primeira reta no formato ax + by = c (Exemplo 2x + 3y = 6 ficará 2 3 6) :")
eq2 = input("digite a equação da segunda reta no formato ax + by = c (Exemplo 5x + 2y = 2 ficará 5 2 2) :")

a1, b1, c1 = [float(x) for x in eq1.split()]
a2, b2, c2 = [float(x) for x in eq2.split()]


v1 = (b1, -a1)
v2 = (b2, -a2)

if v1[0]*v2[1] - v1[1]*v2[0] == 0:
    print("As retas são paralelas.")
else:
    p1 = (c2*b1 - c1*b2) / (a1*b2 - a2*b1)
    p2 = (c2*a1 - c1*a2) / (b1*a2 - b2*a1)
    print(f"As retas se encontram no ponto ({p1}, {p2}).")