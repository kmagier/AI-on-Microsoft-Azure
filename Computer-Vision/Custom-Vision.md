### Custom Vision

#### 1. Przedstawienie usługi

Usługa Custom Vision jest usługą rozpoznawania obrazów, pozwalającą budować oraz wdrażać oraz ulepszać swoje własne identyfikatory. Identyfikator obrazów przypisuje etykiety(reprezentujące klasy lub obiekty) do obrazów, na podstawie ich charakterystyki. W odróżnieniu od usługi Computer Vision, pozwala na określenie etykiet oraz na uczenie własnych modeli do wykrywania tych etykiet.

#### 2. Przykłady użycia

Przykładowe przypadki użycia:

* Program pozwalający rozpoznawać gatunki zwierząt lub roślin
* Program do rozpoznawania modeli ubrań na podstawie zdjęcia modela
* Program do rozpoznawania potraw na podstawie zdjęć

#### 3.How to

Usługa udostępnia interfejs API za pomocą którego możemy trenować modele oraz otrzymywać wyniki klasyfikacji będące wynikiem działania naszego modelu.

Modelami oraz treningiem możemy zarządzać również z poziomu platformy customvision.ai, na której możemy stworzyć bazę danych uczących dla naszego modelu, wytrenować model, oraz sprawdzić dokładność wytrenowanego modelu. W utworzonej bazie obrazów, użytkownik sam określa jakie cechy obrazu go interesują oraz nadaje im odpowiednie nazwy.

Funkcjonalność usługi możemy podzielić na klasyfikację obrazów oraz detekcję obiektów.

W klasyfikacji obrazów, do danego obrazu przypisywane są pasujące do niego etykiety.

W detekcji obiektów również przypisywane są etykiety, a dodatkowo wyznaczane jest położenie obiektów, do których dane etykiety zostały przyporządkowane.

Usługa jest zoptymalizowana do szybkiego rozpoznawania różnić pomiędzy obrazami. Prototypy można tworzyć korzystając z niewielkiej ilości danych, jednak usługa nie jest optymalna w operacjach wykrywania niewielkich różnic pomiędzy obrazami.

#### 4. Pricing

Usługa dostępna jest w dwóch wariantach: **Free** oraz **Standard**.

Wariant **Free**:

* Dozwolone 2 transakcje na sekundę
* Transakcje wgrywania, trenowania oraz predykcji dozwolone są dla 5000 obrazów treningowych dla jednego projektu
* Maksymalnie dwa projekty
* Do 1 godziny uczenia modelu miesięcznie
* Do 10000 predykcji miesięcznie

Wariant **Standard**:

* Transakcje wgrywania oraz predykcji - $2 za 1000 transakcji
* Uczenie - $20 za godzinę obliczeniową
* Maksymalnie 100 projektów
* Przechowywanie obrazów - $0.70 za 1000 obrazów, o maksymalnym rozmiarze 6 MB