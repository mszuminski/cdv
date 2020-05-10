#pi
import math
pi=math.pi
print(pi)

#pierwiastek
x=math.sqrt(9)
print(x)

#losowanie
import random
rand=random.random()
print(rand)

list=random.choice([1,2,3,4,5,6])
print(list)

'''
Użytkownik podaje z klawiatury liczbę całkowitą z zakresu <1;10>
Sprawdź czy liczba jest prawidłowa:
tak) wylosuj liczbę z podanego zakresu
    porównaj liczbę wylosowaną z liczbą podaną przez użytkownika
    wartość ("Gratulacje" lub "Spróbuj innym razem")
nie) poinformuj uzytkownika o błędzie
'''

x=input("Sprobuj zgadnąć liczbe calkowita z zakresu od 1 do 10: ")
x=int(x)
if x<=10 and x>=1:
    losuj=random.choice([1,2,3,4,5,6,7,8,9,10])
    if losuj==x:
        print("Gratulację")
    else:
        print("Spróbuj innym razem, liczba to: " +str(losuj))
else:
    print("Podałeś błędną liczbę")