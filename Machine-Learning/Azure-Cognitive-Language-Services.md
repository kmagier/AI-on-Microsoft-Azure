### Azure Cognitive Language Services

#### 1. Content Moderator

##### 1.1. Przedstawienie usługi

Usługa Azure Content Moderator zapewnia wspomagane maszynowo moderowanie zawartości obrazów, tekstów i filmów wideo.

Najczęstszym zastosowaniem usługi jest moderowanie tekstu:

- Pokoje rozmów(chaty)
- Fora dyskusyjne
- Chatboty
- Dokumenty

Usługa Azure Content Moderator analizuje tekst wyszukując w nim

* Potencjalnie niepożądanych wyrazów
* Wrażliwe dane osobowe(adres e-mail, adres IP, numery ubezpieczenia/PESEL itd.)

Na podstawie analizy, usługa zwraca informacje o występujących niepożądanych wyrazach i ich typie oraz ogólną klasyfikację całego tekstu na podstawie dopasowania do trzech możliwych kategorii:

* **Kategoria 1**: Potencjalna obecność języka, który może zostać uznany za jednoznacznie seksualny lub dla dorosłych.
* **Kategoria 2:** Potencjalna obecność języka, który w pewnych sytuacjach może zostać uznany za dwuznaczny lub dla dorosłych.
* **Kategoria 3:** Potencjalna obecność języka, który może zostać uznany za obraźliwy.

Po analizie tekstu, usługa zwraca informację o wyniku dopasowania tekstu do danej kategorii w skali 0-1 pkt. Im bliżej wartości 1, tym większe dopasowanie do danej kategorii.

##### 1.2. Przypadki użycia

Przykładowe przypadki użycia:

* Chatbot dla Sanepidu, odpowiadający na najczęściej zadawane pytania; do wykrywania potencjalnie niepożądanych, obraźliwych treści
* Analiza sekcji komentarzy pod artykułami i informacjami udostępnianymi na stronie tvp.info; do wykrywania potencjalnie niepożądanych, obraźliwych treści
* W systemie ankietyzacji na Wydziale Elektrycznym, do wykrywania potencjalnie niepożądanych, obraźliwych treści

##### 1.3. How to

Aby użyć serwisu, należy stworzyć nowy zasób na platformie Azure. W Azure Marketplace należy wyszukać usługi Content Moderator, a następnie ją utworzyć.

Po utworzeniu usługi, można się z nią komunikować poprzez API z wykorzystaniem klucza, które można uzyskać w ustawieniach usługi.

Używając klucza oraz podanego endpointu, po wysłaniu tekstu do analizy, usługa wysyła odpowiedź w formacie JSON, w której podane są informacje o wykrytych potencjalnie niepożądanych treściach, lub danych wrażliwych.

##### 1.4. Pricing

Usługa dostępna jest w dwóch wariantach cenowych: **Free** oraz **Standard**

Wariant Free:

* Możliwa 1 transakcja/sekunda
* 5000 darmowych transakcji/miesiąc

Wariant Standard:

* Możliwe 10 transakcji/sekunda
* Cena w zależności od ilości wykonanych transakcji:
  * 0-1M - $1 za 1000 transakcji
  * 1-5M - $0.75 za 1000 transakcji
  * 5-10M - $0.6 za 1000 transakcji
  * 10M+ - $0.4 za 1000 transakcji

#### 2. Language Understanding Intelligent Service

##### 2.1. Przedstawienie usługi

Language Understanding Intelligent Service(LUIS) jest narzędziem wykorzystującym przetwarzanie języka naturalnego do zrozumienia ludzkiego języka w aplikacjach użytkownika, na stronach internetowych, w chatbotach itd.

Usługa wykorzystuje trzy kluczowe aspekty dla zrozumienia języka:

* **Wypowiedzi:** wypowiedź to dane wejściowe od użytkownika, które aplikacja musi zinterpretować.
* **Intencje:** intencja reprezentuje zadanie lub działanie, które użytkownik chce wykonać. Jest to zamiar lub cel wyrażony w wypowiedzi użytkownika.
* **Encje:** encja reprezentuje słowo lub frazę w wypowiedzi, którą chcesz wyodrębnić.

##### 2.2. Przypadki użycia

Przykładowe przypadki użycia:

* Chatbot wspomagający rejestrację do lekarza: np. po wpisaniu przez użytkownika frazy: "Jak mogę się zarejestrować do lekarza?" bot może zwrócić link do strony z niezbędnymi informacjami lub listą lekarzy i sposobem kontaktu
* W wyszukiwarce sklepów internetowych; która na podstawie zapytania np. "Gdzie kupię skarpetki w Warszawie", zwróci listę sklepów z ich adresem.

##### 2.3. How to

Aby użyć serwisu, należy stworzyć nowy zasób na platformie Azure. W Azure Marketplace należy wyszukać usługi Language Understanding, a następnie ją utworzyć.

Następnie należy utworzyć aplikację LUIS pod jednym z dostępnych adresów, zależnych od regionu, w którym została utworzona usługa.

Po utworzeniu aplikacji należy dodawać intencje, wypowiedzi oraz encje. Następnie należy "nauczyć" aplikację wyboru podmiotu zdań; w dodanych wypowiedziach należy podkreślić co jest podmiotem w danym zdaniu i przypisać go do encji. Po tym należy użyć opcji **Train**, by wytrenować model, a następnie upublicznić aplikację, by możliwe było korzystanie z niej.

##### 2.4. Pricing

Usługa dostępna jest w dwóch wariantach **Free** oraz **Standard**:

Wariant **Free**:

* Możliwe 5 transakcja/sekunda
* Zapytania tekstowe - 10000 transakcji/miesiąc
* Transakcje autorskie - 1M transakcji/miesiąc

Wariant **Standard**:

* Możliwe 50 transakcji/sekunda
* Zapytania tekstowe - $1.50 za 1000 transakcji
* Zapytania z użyciem mowy - $5.50 za 1000 transakcji

#### 3. Text Analytics API

##### 3.1. Przedstawienie usługi

Usługa Text Analytics API jest jedną z usług wchodzących w skład Cognitive Services. Została stworzona, by ułatwić pozyskiwanie informacji z tekstu. Z jej pomoca można zidentyfikować język, opinię, wyróżnić kluczowe frazy oraz rozpoznać encje w tekście.

##### 3.2. Przypadki użycia

* Do analizy nastrojów społecznych na podstawie sekcji komentarzy pod profilem na twitterze/facebook'u partii politycznej lub urzędu
* Do rozpoznawania języka w translatorze internetowym(gdy nie wiemy w jakim języku napisany jest tekst, który chcemy tłumaczyć)

##### 3.3. How to

Aby użyć serwisu, należy stworzyć nowy zasób na platformie Azure. W Azure Marketplace należy wyszukać usługi Text Analytics, a następnie ją utworzyć.

Po utworzeniu usługi, korzystając z jej klucza, możemy wysyłać zapytania pod endpoint określający funkcję usługi, z której chcemy skorzystać, tj. identyfikacja języka, opinii, podział na frazy kluczowe lub rozpoznawanie encji.

Po wysłaniu zapytania otrzymujemy odpowiedź w formacie JSON, która zawiera informacje:

* dla usługi rozpoznawania języka, zwraca informację o tym, w jakim języku został napisany tekst oraz wartość dopasowania
* dla usługi identyfikacji opinii, zwraca informację o tym, czy opinia jest negatywna(wartość 0-0.49), czy opinia jest neutralna(wartość 0.5), czy pozytywna(wartość 0.5+)
* dla usługi wyróżniającej frazy kluczowe, zwraca listę kluczowych fraz znalezionych w danym dokumencie
* dla usługi rozpoznawania encji, zwraca rozpoznane encje wraz z ich kategoriami i podkategoriami

##### 3.4. Pricing

Usługa dostępna jest w kilku wariantach **Free**, **Standard**, **S0**, **S1**, **S2**, **S3**, **S4** :

Wariant **Free**:

* 5000 transakcji/miesiąc

Wariant **Standard**:

* 0-500 000 rekordów tekstowych - $2 za 1000 rekordów
* 0.5M-2.5M rekordów tekstowych - $1 za 1000 rekordów
* 2.5M-10M rekordów tekstowych - $0.5 za 1000 rekordów
* 10M+ rekordów tekstowych - $0.25 za 1000 rekordów

Warianty **S0**-**S4** wymagają stałej miesięcznej opłaty w ramach której do wykorzystania jest konkretna ilość transakcji w miesiącu; po przekroczeniu której opłata naliczana jest za każde kolejne 1000 transakcji, przy czym najtańszą opcją jest wariant **S0** (natomiast za każde 1000 transakcji powyżej limitu płacimy najwięcej), natomiast najdroższym wariantem jest **S4** (jednak opłata za transakcje powyżej limitu jest najniższa)



