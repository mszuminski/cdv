#listy
progr=['PHP','Python']
print(type(progr))
progr.append('C#')
print(progr)
count=progr.count('PHP')
print(f'PHP występuje {count} razy\n')

#tuple
name=('Krystyna', 'Anna')
print(name)
print(type(name))
first=name[0]
print(first)
#name.append('Janusz') - nie można dodawać
print()

#słowniki
person={
    'name':'Anna',
    'surname':'Nowak'
}

print(person)
print(type(person))
print(person['name'])
print(person.keys())
print(person.get('height', 'brak danych')) #sprawdza czy istnieje i wyświetla odpowiednią wartość

person['height']=178
print(person.get('height', 'brak danych'))

print()

'''
Utwórz słownik i przypisz mu trzy imiona podane z klawiatury
wyświetl te dane na ekranie w formacie:
Imię1: ...
Imię2: ...
Imię3: ...
'''
imiona={
    '0':'',
    '1':'',
    '2':''
}
name1=input("Podaj pierwsze imię: ")
name2=input("Podaj drugie imię: ")
name3=input("Podaj trzecie imię: ")

imiona['0']=name1
imiona['1']=name2
imiona['2']=name3

for key, value in imiona.items():
    count=int(key)+1
    print(f'Imię{count}: {value}')