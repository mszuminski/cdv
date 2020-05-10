progr=['Python', 'PHP', 'C#', 'JS', 'Java']
print(progr)
print(type(progr))

first=progr[0]
print(first)

threeElements=progr[0:3]
print(threeElements)

last=progr[-1]
print(last)

#Dodanie nowego elementu na koniec listy
progr.append('R')
progr.append('Python')
print(progr)

#zliczanie elementu (konkretnego) w liście
countElement=progr.count('Java')
print(countElement)

#ilosc elementów w liście
countElementsOfList=len(progr)
print(countElementsOfList)

#połączenie list
anotherList=['C','C++']
progr.extend(anotherList)
print('progr: ' +str(progr))
print('anotherList: ' +str(anotherList))

#usuwanie elementów z listy
new=progr
print('New list: ' +str(new))
new.clear()
print('New list: ' +str(new))
print('Rozmiar New list: ' +str(len(new)))
print('progr list: ' +str(progr))
print('Rozmiar progr list: ' +str(len(progr)))

x=8
print(x)
y=x
print(y)

y=5
print(x) #8
print(y) #5

'''
Dodaj liste o nazwie: country
Przypisz do niej 5 elementów
Poproś użytkownika, aby dodał dwa nowe elementy do listy
Użytkownikowi wyświetl listę do wyboru:

1) Wyświetl pierwsze 3 elementy listy
2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)
3) Wyświetl zawartośc listy
4) Wyczyść zawartość listy
5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)

Użytkownik raz dokonuje wyboru z listy.
Wyświetl zawartość listy po wykonaniu operacji przez użytkownika.
'''

country=['kraj1', 'kraj2', 'kraj3', 'kraj4', 'kraj5']
print("Dodaj 2 elementy do listy: ")
dodaj1=input("Pierwszy element: ")
dodaj2=input("Drugi element: ")
country.append(dodaj1)
country.append(dodaj2)

print("Co chcesz zrobić: ")
print("1) Wyświetl pierwsze 3 elementy listy")
print("2) Wyświetl elementy listy, które dodałem (dane pobierz z listy)")
print("3) Wyświetl zawartośc listy")
print("4) Wyczyść zawartość listy")
print("5) Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy)")
print("0) Kończy działanie programu")
wybor=input("Wybierasz: ")

while wybor!=0:
    wybor=int(wybor)
    if wybor==1:   
        print(country[0:3])
        wybor=input("Wybierasz: ")
    elif wybor==2:
        print(country[-2])
        print(country[-1])
        wybor=input("Wybierasz: ")
    elif wybor==3:
        print(country)
        wybor=input("Wybierasz: ")
    elif wybor==4:
        country.clear()
        print(country)
        wybor=input("Wybierasz: ")
    elif wybor==5:
        szukaj=input("Podaj szukany element: ")
        countElement=country.count(szukaj)
        if countElement==1:
            print("Podany element istnieje na liście")
        else:
            print("Podany element nie istnieje na liście")
        wybor=input("Wybierasz: ")
    elif wybor==0:
        print("Koniec działania")        
    else:
        print("Wybrano złą wartość")