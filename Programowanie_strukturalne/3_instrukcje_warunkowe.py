x=6

if x==5:
    print("x jest równy 5")
else:
    print("x nie jest równy 5")
    print("x jest równy: " + str(x))

print("Koniec instrukcji warunkowej")


##########################################

y=False
if y:
    print("Prawda")
else:
    print("Fałsz")

##########################################

z = 5 > 6
if z:
    print("Prawda")
else:
    print("Fałsz")


'''
Uzytkownik podaje wartosci trzech zmiennych: x, y, z
Wyswietl ktora z tych wartosci bedzie najwieksza,
wykorzystaj instrukcje warunkow
'''
x=input("Podaj wartosc liczby x:")
y=input("Podaj wartosc liczby y:")
z=input("Podaj wartosc liczby z:")

if x>y and x>z:
    print("Najwieksza wartosc wynosi: " + str(x))
elif y>x and y>z:
    print("Najwieksza wartosc wynosi: " + str(y))
elif z>x and z>y:
    print("Najwieksza wartosc wynosi: " + str(z))   

