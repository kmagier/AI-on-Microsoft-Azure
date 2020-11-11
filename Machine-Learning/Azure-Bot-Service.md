### Azure Bot Service

#### 1. Przedstawienie usługi

Usługa Azure Bot Service zapewnia niezbędne komponenty do tworzenia botów, oraz niezbędne usługi do łączenia botów z kanałami.

Głównym zastosowaniem usługi Bot Service jest tworzenie botów do konwersacji z użytkownikiem, z wykorzystaniem AI.

#### 2. Przykłady użycia

Przykładowe przypadki użycia:

* Wsparcie klienta dotyczące produktów lub usług(np. w sklepie internetowym)
* Systemy rezerwacji, np. w restauracji, kinach, hotelach, rezerwacje biletów lotniczych itp.
* Konsultacje lekarskie oraz w samodzielnej diagnozie
* Automatyzacja w domu; cyfrowy asystent

#### 3.How to

Bota można utworzyć na kilka sposobów oraz zintegrować go z wieloma usługami z kategorii Cognitive Services dotyczącymi rozpoznawania mowy, tekstu, obrazu itd.

##### 3.1. QnA Maker

QnA Maker jest serwisem wykorzystującym NLP(Natural Language Processing), dzięki czemu pozwala na prowadzenie naturalnej konwersacji. Wykorzystywany jest do znalezienia najbardziej odpowiedniej odpowiedzi na zadane przez użytkownika pytanie, korzystając z bazy wiedzy(KB - knowledge base).

Usługa najczęściej wykorzystywana jest do tworzenia aplikacji konwersacyjnych, głównie w social mediach i czat botach.

Usługi QnA Maker warto użyć kiedy:

* Kiedy przechowujesz statyczne informacje - bazę wiedzy odpowiedzi można zbudować z plików takich jak .doc, .pdf, jak również ze źródeł internetowych podając URL
* Kiedy chcesz, by odpowiedź na to samo pytanie, prośbę, komendę była taka sama niezależnie od użytkownika, który je zadaje
* Jeśli chcesz zarządzać konwersacją zawierającą informacje statyczne - baza wiedzy pobiera tekst konwersacji lub polecenie i odpowiada na nie na podstawie informacji zawartych w bazie. Odpowiedź może również zawierać informacje statyczne, będące częścią ustalonego przepływu konwersacji, bot może zapewnić ten przepływ.

Baza Wiedzy(Knowledge Base):

QnA Maker posługuje się bazą wiedzy, która jest zbiorem par pytanie-odpowiedź. Wcześniej przygotowane bazy wiedzy można łatwo importować, a usługa określi relację pomiędzy odpowiednimi częściami zawartości importowanego pliku.

W usłudze QnA Maker bota można stworzyć korzystając wyłącznie z odpowiedniego portalu, jak również korzystając z gotowych bibliotek dla kilku języków programowania.

##### 3.2. Bot Framework Composer

Bot Framework Composer jest narzędziem typu open-source do tworzenia botów. Łączy w sobie usługi rozpoznawania języka tj. LUIS oraz QnA Makera. Jest dostępny jako aplikacja desktopowa jak również jako aplikacja webowa.

Bot Framework Composer pozwala na tworzenie przepływów konwersacji, za pomocą edytora graficznego. Posiada narzędzia do zarządzania rozpoznawaniem języka oraz komponentami pochodzącymi z QnA Makera.

Dzięki narzędziu Bot Framework Composer możliwe jest:

* Tworzenie botów bez potrzeby pisania jakiegokolwiek kodu
* Wdrażanie danych skojarzonych z NLP jako modeli LUIS oraz baz danych QnA Makera
* Tworzenie botów w wielu językach
* Wdrażanie botów do usług **Azure App Service** oraz **Azure Functions**

#### 4. Pricing

Usługa dostępna jest w dwóch wariantach: **Free** oraz **S1**, które różnią się w zależności od używanych kanałów: 

* Kanały standardowe - serwisy, które mają publicznie dostępny klucz Bot API(np. Facebook oraz Slack)
* Kanały premium - pozostałe serwisy, w tym serwisy prywatne

Wariant **Free**:

* Kanały standardowe - nielimitowana ilość wiadomości
* Kanały premium - 10 000 wiadomości/miesiąc

Wariant **S1**:

* Kanały standardowe - nielimitowana ilość wiadomości
* Kanały premium - $0.50 za 1000 wiadomości