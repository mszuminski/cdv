slownik = {'key1':'value1', 'key2':'value2'}

'''
Utwórz słownik o nazwie pracownik zawierający następujące klucze:
imie, nazwisko, miasto, wiek, imionaDzieci (podaj dwa imiona),
imiona rodziców (podaj dwa imiona)
'''

pracownik = {
    'name':'Anna',
    'surname':'Nowak',
    'city':'Poznań',
    'age':20,
    'namesChildren':['Tomasz', 'Krystyna'],
    'namesParent':['Paweł', 'Katarzyna']
}

print(pracownik)
print(pracownik['namesChildren'])
print(pracownik['namesChildren'][0])

pracownik['height'] = 180
pracownik['weight'] = 80
print(pracownik)

key='age'
if key in pracownik:
    del pracownik[key]
    print(f'Klucz {key} został usunięty')
else: 
    print(f'Klucz o nazwie {key} nie znaleziono w słowniku pracownik')

print(pracownik)

print(pracownik.values())
print(list(pracownik.values()))
print(pracownik.items())

'''
Wyświetl za pomocą pętli for wartości i klucze ze słownika pracownik
w formacie: klucz:wartość
Wykorzystaj w pętli for funkcję print do wyświetlenia danych
'''

for key, value in pracownik.items():
    print(f'{key}:{value}')

