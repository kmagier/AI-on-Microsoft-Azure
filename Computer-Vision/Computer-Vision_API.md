### Computer Vision API	

#### 1. Przedstawienie usługi

Usługa Computer Vision zapewnia dostęp do wielu algorytmów pozwalających na przetwarzanie obrazów i uzyskiwaniu z nich informacji na podstawie cech, które są dla nas interesujące. Usługa pozwala na określenie, czy obraz zawiera treści przeznaczone dla dorosłych, pozwala rozpoznać marki produktów, różne obiekty, a także ludzkie twarze.

#### 2. Przykłady użycia

Przykładowe przypadki użycia:

* Program pozwalający rozpoznać miejsce, w którym zostało wykonane zdjęcie na podstawie cech charakterystycznych
* Program wspierający pracę policji do rozpoznawania osób poszukiwanych
* Program pozwalający odczytywać pismo lekarzy na receptach

#### 3.How to

Usługa Computer Vision udostępnia interfejs API, za pomocą którego możemy wysyłać zapytania, oraz odbierać wyniki działania konkretnego algorytmu, w formacie JSON.

##### 3.1. OCR

Usługa posiada możliwości rozpoznawania znaków (OCR - Optical Character Recognition). Za pomocą Read API możliwe jest wydobycie z pisma ręcznego oraz drukowanego poszczególnych liter oraz słów. Odczyt możliwy jest z rachunków, plakatów, wizytówek, listów, tablic itd. Usługa wspiera wydobywanie tekstu w wielu językach.

##### 3.2. Rozpoznawanie cech

Usługa pozwala na wydobywanie z obrazów cech wizualnych, spośród wielu tysięcy rozpoznawalnych obiektów, takich jak scenerie, żywa natura oraz akcje. Rozpoznane cechy można opisać tagami a jeśli nie można tego zrobić jednoznacznie, usługa zapewnia podpowiedzi określające kontekst.

##### 3.3. Rozpoznawanie obiektów

Usługa pozwala na detekcję obiektów na obrazie. Wykorzystując algorytm, usługa pozwala na przetwarzanym obrazie zaznaczyć położenie wykrytego obiektu za pomocą prostokąta, a także pozwala rozpoznać i nazwać wykryty obiekt.

##### 3.4. Rozpoznawanie twarzy

Usługa zawiera rozbudowane API do wykrywania, rozpoznawania i analizowania ludzkich twarzy zawartych na obrazach. 

* Rozpoznawanie twarzy - usługa pozwala wykrywać ludzkie twarze i oznaczać ich położenie na obrazie. Opcjonalnie usługa pozwala na wydobywanie cech związanych z twarzą, takich jak części twarzy, a także określić płeć, wiek, emocję itd.
* Weryfikacja twarzy - usługa pozwala na weryfikację twarzy; na podstawie posiadanych zdjęć możemy określić, czy dana twarz należy do danej osoby, której twarz znajduje się już w bazie
* Znajdowanie podobieństw - usługa pozwala na znajdowanie podobieństw między danym zdjęciem twarzy, a zbiorem zawierającym wiele zdjęć innych twarzy. Usługa pozwala również na grupowanie zbioru nieznanych twarzy w grupy, opierając się na podobieństwach między nimi

##### 3.5. Moderacja treści

Usługa pozwala na moderowanie treści na podstawie analizy z wykorzystaniem klasyfikatorów. Pozwala określić, czy dany obraz jest przeznaczony dla osób dorosłych, informacja o tym może być częścią mechanizmu automatycznej moderacji treści.

#### 4. Pricing

Usługa dostępna jest w dwóch wariantach: **Free** oraz **S1**, które różnią się ilością dozwolonych transakcji w jednostce czasu oraz dostępnymi opcjami analizy obrazu.

Wariant **Free**:

* Możliwe 20 transakcji na minutę
* Do 5000 transakcji miesięcznie

Wariant **S1**:

* Do 10 transakcji na sekundę
* Dla funkcji Tag, Face, GetThumbnail, Color, Image Type, GetAreaOfInterest cennik zaczyna się od $1 za 1000 transakcji, jeśli w ciągu miesiąca wykona się do 1M transakcji, aż do $0.65 za każde 1000 transakcji powyżej łącznej ilości 5M transakcji
* Dla funkcji OCR, Adult, Celebrity, Landmark, Detect, Objects, Brand od $1.50 za 1000 transakcji, jeśli w ciągu miesiąca wykona się do 1M transakcji, aż do $0.65 za 1000 transakcji powyżej łącznej ilości 5M transakcji
* Dla funkcji Describe, Read $2.50 za 1000 transakcji