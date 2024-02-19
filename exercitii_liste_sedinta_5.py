# 1) Sa se calculeze suma sublistelor din lista my_list si sa se afiseze valoarea totala in consola

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

suma_totala = 0

for i in my_list:
    suma_sublista = sum(i)
    suma_totala += suma_sublista

print("Suma sublistelor din my_list este:", suma_totala)


# 2) Sa se calculze suma tuturor elementelor din lista de mai jos:

l1 = [23, [1, 2, 3, 11, 14, 182,], [4, 1, 2, 3, 5, 6], 12, -3, 4, [7, 8, 9], 2, 3, "123", True, False, 2.5]

suma_totala_elemente = 0

for elem in l1:
    if isinstance(elem, list):
        suma_totala_elemente += sum(elem)
    elif isinstance(elem, str):
        suma_totala_elemente += int(elem)
    elif isinstance(elem, bool):
        if elem == True:
            suma_totala_elemente += 1
    else:
        suma_totala_elemente += elem

print(suma_totala_elemente)

