print("Anna")
print(8)

#potegowanie
pow=2**10
print(pow)

text="cdv"
print(text*2)

#pobieranie danych z klawiatury
# + kontatenacja

name=input("Podaj imię:")
print("Twoje imię: " + name)

surname=input("Podaj swoje nazwisko:")
print("Imię: " +name + ", nazwisko: " + surname)

#camel case - sposób zapisywania zmiennych
lengthName=str(len(name))
print("Długość imienia: " + lengthName)

lengthSurname=str(len(surname))
print("Długośc nazwiska: " + lengthSurname)

print(type(lengthName))
print(type(surname))

#next part
print("\nPodaj narodowość: ", end="")
nationality=input()

surname="Kowalski"
firstLetter=surname[0]
secondLetter=surname[1]
print(firstLetter)
lastLetter=surname[len(surname)-1]
print(lastLetter)

#konwersja typów danych
a="10"
print(type(a))
a=int(a)
print(type(a))

b=6
print(type(b)) #int
b/=2 # = b=b/2 | dzielenie zmienia z int na float
print(type(b)) #float
print(b) #3.0

print()
surname="Nowakowski"
print(surname[0]) #N
print(surname[0:2]) #No
print(surname[-2]) #k
print(surname[-2:]) #ki
print(surname[:-2]) #Nowakows
print(surname[:-2:2]) #Nwkw

