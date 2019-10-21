
#################################
#          MARIUSZ KLUZA        #
#################################
#2.10 Mamy dany napis wielowierszowy line. Poda� spos�b obliczenia liczby wyraz�w w napisie. Przez wyraz rozumiemy ci�g "czarnych" znak�w, oddzielony od innych wyraz�w bia�ymi znakami (spacja, tabulacja, newline).
line = '''abd\tdef\ngh\nij'''
print(line)
print(len(line.split()))

#2.11 Poda� spos�b wy�wietlania napisu word tak, aby jego znaki by�y rozdzielone znakiem podkre�lenia.
print('_'.join('word'))

#2.12 Zbudowa� napis stworzony z pierwszych znak�w wyraz�w z wiersza line. Zbudowa� napis stworzony z ostatnich znak�w wyraz�w z wiersza line.
line = '''abd\tdef\tgh\tij'''

napis = line.split()
pierwsze = list()
ostatnie = list()
for i in range(0, len(napis)):
    pierwsze.append((napis[i])[0])
    ostatnie.append((napis[i])[len(napis[i])-1])

pierwsze = "".join(pierwsze)
ostatnie = "".join(ostatnie)
print(pierwsze)
print(ostatnie)

#2.13 Znale�� ��czn� d�ugo�� wyraz�w w napisie line. Wskaz�wka: mo�na skorzysta� z funkcji sum().
line = '''abd\tdef\tgh\tij'''

napis = line.split()
suma = list()
for i in range(0, len(napis)):
    suma.append(len(napis[i]))

wynik = sum(suma)
print(wynik)
#2.14 Znale��: (a) najd�u�szy wyraz, (b) d�ugo�� najd�u�szego wyrazu w napisie line.
line = '''abd\tdef\tghagh\tij'''

napis = line.split()
napis.sort(key=len)
napis.reverse()
print("Najdluzszy wyraz " '"'+ napis[0] +'"' " ma dlugosc " + str(len(napis[0])))

#2.15 Na li�cie L znajduj� si� liczby ca�kowite dodatnie. Stworzy� napis b�d�cy ci�giem cyfr kolejnych liczb z listy L.
L = [3,53,4,75,2,111,37,4,89]

napis = list()
for i in range(0, len(L)):
    napis.append(str(L[i]))
napis = "".join(napis)
print(napis)

#2.16 W tek�cie znajduj�cym si� w zmiennej line zamieni� ci�g znak�w "GvR" na "Guido van Rossum".
line = "TEXT TEXT GvR TEXT GvR TEXT TEXT TEXT GvR TEXT"

napis = line.replace("GvR", "Guido van Rossum")
print(napis)
#2.17 Posortowa� wyrazy z napisu line raz alfabetycznie, a raz pod wzgl�dem d�ugo�ci. Wskaz�wka: funkcja wbudowana sorted().
line = "pies kot chomik papuga delfin lis"

napis = line.split()
print("Alfabetycznie: " + str(sorted(napis, key=str.lower)))
print("Wedlug dlugosci: " + str(sorted(napis, key=len)))

#2.18 Znale�� liczb� cyfr zero w du�ej liczbie ca�kowitej. Wskaz�wka: zamieni� liczb� na napis.
x = 403424030200040000200123210000

napis = str(x)
n = 0
for i in napis:
    if i == "0":
        n+=1
print("Ilosc cyfr zero w liczbie " + napis + " to " + str(n))

#2.19 Na li�cie L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudowa� napis z trzycyfrowych blok�w, gdzie liczby jedno- i dwucyfrowe b�d� mia�y blok dope�niony zerami, np. 007, 024. Wskaz�wka: str.zfill().
L = [4,54,643,7,5,422,435,55,3,22,323,3]

napis = list()
for i in range(0, len(L)):
    a = (str(L[i])).zfill(3)
    napis.append(a)
print(napis)

input()