Projekt zaliczeniowy: Katalog film�w			
Autor: Mariusz Kluza			
Data: 10.02.2020			

######################################### 
Informacje og�lne:

Projekt realizuje implementacj� katalogu film�w z wykorzystaniem j�zyka Python3 i baz danych SQLite. 

######################################### 
Uruchamianie:

Aby uruchomi� program nale�y u�y� komendy:
>>> python run.py

Podczas uruchomienia program automatycznie (przy u�yciu pip) instaluje bibliotek� niezb�dn� do poprawnego wy�wietlania danych. Biblioteka ta mo�e zosta� automatycznie odinstalowana podczas zamykania programu, wedle �yczenia u�ytkownika.

######################################### 
Zawarto��:

README.txt 
Plik tekstowy zawieraj�cy dokumentacj�.

run.py
Plik uruchamiaj�cy aplikacje, zawieraj�cy g��wn� p�tle programu.

my_functions.py
Plik zawieraj�cy wszystkie funkcje u�yte w programie.

movies.db
Przyk�adowa baza danych.

######################################### 
Metody:

my_connect()
Metoda najpierw pyta o nazw� bazy danych (bez rozszerzenia!), z kt�r� chcemy si� po��czy� (je�li baza o podanej nazwie nie istnieje, tworzona jest automatycznie nowa baza). Nast�pnie tworzy po��czenie z baz� oraz tworzy obiekt kursora niezb�dny do wykonywania opercaji na bazie.


my_create()
Metoda tworzy tabel� o ustalonych odg�rnie kolumnach i zapisuje j� do bazy.


my_menu()
Metoda wy�wietlaj�ca opcj� panelu g��wnego aplikacji.


my_table()
Metoda pobiera jako argument list� rekord�w. U�ywaj�c biblioteki 'texttable' (s�u��cej do wizulanej prezentacji danych) tworzy tabel� o odpowiednich nag��wkach, a nast�pnie przechodz�c po kolejnych rekordach listy, dodaje dane do tabeli, kt�r� na koniec wy�wietla.


my_add()
Metoda s�u�y do dodania nowej pozycji do bazy danych. Kolejno pyta o: tytu� (niezb�dny), gatunek, czas trwania, re�ysera, kraj produkcji oraz rok produkcji. Nas�t�pnie dodaje wpisane dane do bazy, zapisuje i wy�wietla odpowiedni komunikat.


my_edit()
Metoda s�u�y do edycji istniej�cych pozycji w bazie. Na pocz�tku wywo�uje metod� my_show(), aby pokaza� istniej�ce w bazie filmy. Nastepnie pyta o ID filmu, kt�ry chcemy edytowa� (je�li ID nie istnieje to wy�wietla odpowiedni komunikat). Po wybraniu odpowiedniego ID wy�wietla list� opcji jakich mo�emy u�y� do edycji filmu. Po wybraniu i zatwierdzeniu zmiany wywo�uje metode my_save. W metodzie zawarta jest niesko�czona p�tla, kt�r� opu�ci� mo�na wybieraj�c odpowiedni� opcj� ("Powr�t").


my_save()
Metoda jako argument przyjmuje ID filmu kt�ry zosta� edytowany. Zapisuje dane zmiany do bazy i wy�wietla odpowiedni komunikat.


my_delete()
Metoda s�u�y do usuni�cia istniej�cej pozycji z bazy. Na pocz�tku wywo�uje metod� my_show(), aby pokaza� istniej�ce w bazie filmy. Nastepnie pyta o ID filmu, kt�ry chcemy usun�� (je�li ID nie istnieje to wy�wietla odpowiedni komunikat). Po wybraniu odpowiedniego ID wy�wietla komunikat pytaj�cy o potwierdzenie naszej decyzji. Zale�nie od wyboru albo pozostawia film w bazie i wraca do panelu g��wnego, albo usuwa rekord z bazy, zapisuje zmiany i wy�wietla odpowiedni komunikat.


my_search()
Funkcja filtruje i wy�wietla filmy zapisane w bazie. Mo�e wy�wietli� wszystkie rekordy (my_show()) lub odpowiednio je przefiltrowa� po: tytule, gatunku czy re�yserze. Trzy ostatnie opcje przekierowuj� nas do odpowiednich fukcji pomocniczych. Na koniec przekazuje otrzymane rekordy do metody my_table.


my_search_title(), my_search_genre(), my_search_director()
Funkcje nak�adj� odpowiednie filtry. Wywo�uj� fukj� is_empty i zwracaj� odpowiednie wyniki. 


is_empty()
Funkcja sprawdza czy istnieje chocia� jeden rekord spe�niaj�cy na�o�one warunki, wy�wietla odpowiedni komunikat i zwraca odpowiedni� warto�� logiczn�.


my_show()
Metoda wy�wietla wszystkie filmy znajduj�ce si� w bazie. Wy�witla ilo�� wszystkich zapisanych rekord�w, a na koniec przekazuje otrzymane rekordy do metody my_table.


my_drop()
Metoda s�u�y do usuwania wszystkich rekord�w z bazy czyli do czyszczenia ca�ego katalogu. Wy�wietla komunikat pytaj�cy o potwierdzenie naszej decyzji. Zale�nie od wyboru albo wraca do panelu g��wnego, albo usuwa ca�� tablice z bazy i wywo�uje metod� my_create(). Nastepnie zapisuje zmiany i wy�wietla odpowiedni komunikat.


my_exit()
Metoda zamykaj�ca program. Wy�wietla komunikat �egnaj�cy i ko�czy dzia�anie programu.