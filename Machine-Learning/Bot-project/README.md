Ten folder zawiera projekt bota stworzonego przy użyciu Bot Framework Composer.

By przetestować działanie bota lokalnie, należy otworzyć ten folder w aplikacji Bot Framework Composer a następnie kliknąć na "Start Bot".

## Projekt - Bot wspomagający pracę dziekanatu

##### 1. Use case

Utworzony bot ma wspomagać pracę dziekanatu Wydziału Elektrycznego. Bot na podstawie kilku pytań, pomaga użytkownikowi otrzymać informację nt. z kim powinien sie kontaktować w celu rozwiązania swoich problemów na podstawie swojego kierunku studiów, stopnia studiów, trybu studiów oraz posiadania lub braku statusu studenta. Użytkownik, po przejściu całej przygotowanej ścieżki, w wyniku otrzymuje odpowiedź nt. tego z kim konkretnie powinien się skontaktować, wraz z informacjami kontaktowymi, lub jak może pewne problemy rozwiązać korzystając z funkcjonalności internetowego systemu obsługi dziekanatu ISOD.

Bot zakłada następujące scenariusze:

1. Użytkownik chce złożyć wniosek, ale nie wie jak, oraz nie wie jakie są wnioski
2. Użytkownik chce się skontaktować z pracownikiem dziekanatu, ale nie wie z kim konkretnie
3. Użytkownik chce się skontaktować z prodziekanem, ale nie wie jak powinen to zrobić

Pierwszym etapem jest zapytanie użytkownika, którą z powyższych czynności chce wykonać: 

- Złożyć wniosek
- Skontaktować się z pracownikiem dziekanatu
- Skontaktować się z prodziekanem

Następnie w zależności od wybranej opcji:

1. Dla opcji złożenia wniosku, bot wyświetla wszystkie możliwe wnioski i prosi użytkownika o wybranie konkretnego wniosku, nastepnie bot prosi o informację o posiadaniu lub braku statusu studenta. Jeżeli użytkownik ma status studenta, otrzymuje informację o tym, że wniosek można złożyć przez ISOD; jeżeli użytkownik nie posiada statusu, otrzymuje informację, skąd można pobrać wniosek i jak go można złożyć
2. Dla opcji kontaktu z pracownikiem dziekanatu, użytkownik musi odpowiedzieć na serię pytań z sugerowanymi odpowiedziami, które mają doprowadzić do nakierowania użytkownika na odpowiednią osobę. Po określeniu swojego typu studiów, stopnia oraz kierunku, użytkownik otrzymuje kontakt do pracownika dziekanatu, z którym powinien się skontaktować.
3. Dla opcji kontaktu z prodziekanem, użytkownik musi odpowiedzieć na pytanie dotyczące posiadania lub braku statusu studenta. Jeżeli posiada status studenta - otrzymuje informację o tym, jak może się zapisać na konsultacje za pośrednictwem systemu ISOD, jeśli nie, musi parę pytań(podać swoje imię i nazwisko, numer albumu i e-mail), następnie na podstawie tych informacji otrzymuje numerek w systemie konsultacji oraz potwierdzenie na podany adres e-mail.

##### 2. Architektura

Bot składa się głównego dialogu nazwanego **Bot-project** oraz z 10 innych dialogów, z których 7 dialogów odpowiada za kolejne etapy przepływu, pozwalające uzyskać od użytkownika coraz bardziej szczegółowe informacje, oraz 3 dialogi pomocnicze, dla pomocy, akcji rozpoczynającej zadawanie pytań przez bota oraz dla opcji anulowania dialogu, gdyby użytkownik chciał rozpocząć interakcję z botem od początku.

Specyfikacja dialogów i triggerów:

1. **Dialog Bot-project**

   Zawiera 4 triggery; jeden o nazwie **Greeting**, który reaguje po nawiązaniu kontaktu odpowiada wiadomością powitalną, oraz 3 pomocnicze: 

   * **pomoc** - który po wpisaniu frazy "pomoc" wyświetla informację, by podążać za wskazanymi propozycjami, oraz, że możliwe jest rozpoczęcie interakcji od początku po wpisaniu frazy "anuluj".
   * **start** - który uruchamia przepływ po wpisaniu frazy "start"
   * **anuluj** - który pozwala użytkownikowi rozpocząć rozmowę od początku, kasując wszystkie dotychczas zebrane informacje

2. Dialog **Pracownik**

   Dialog uruchamiany jest po wybraniu opcji "Konsultacja z pracownikiem". Zawiera zapytanie  **Prompt with multi-choice** do użytkownika dotyczące trybu studiów(stacjonarne lub niestacjonarne). Na podstawie odpowiedzi z wykorzystaniem instrukcji **Switch **podejmuje decyzję:

   * Jeżeli studia stacjonarne, to kieruje do dialogu, **KonsultacjePracownik**, który zawiera kolejne pytania, pozwalające zebrać więcej informacji o użytkowniku
   * Jeżeli studia niestacjonarne, to bot zwraca dane kontaktowe pracownika odpowiedzialnego za studia niestacjonarne na Wydziale Elektrycznym, ponieważ obecnie zajmuje się tym jeden pracownik.

3. Dialog **KonsultacjePracownik**

   Użytkownik przechodzi do tego dialogu, z dialogu **Pracownik**, w którym musiał odpowiedzieć na pytanie dotyczące trybu studiów. W tym dialogu użytkownik określa w elemencie **Prompt with multi-choice** swój stopień studiów(inżynierskie, magisterskie, doktoranckie), następnie w zależności od wyboru, korzystając z instrukcji **Switch** przenoszony jest do jednego z trzech dialogów **KonsultacjeInz**, **KonsultacjeMgr** lub **KonsultacjeDr**

4. Dialog **KonsultacjeInz**

   Dialog dla użytkowników będących studentami studiów inżynierskich. Użytkownik przechodzi do tego dialogu z dialogu **KonsultacjePracownik**, na tym etapie bot ma informację o trybie studiów oraz o stopniu. W tym dialogu użytkownik w elemencie **Prompt with multi-choice** określa swój kierunek studiów. Po wybraniu kierunku studiów, użytkownikowi zwracana jest informacja z danymi kontaktowymi do pracownika, z którym powinien się kontaktować.

5. Dialog **KonsultacjeMgr**

   Dialog dla użytkowników będących studentami studiów magisterskich. Reszta analogicznie jak w dialogu **KonsultacjeInz**

6. Dialog**KonsultacjeDr**

   Dialog dla użytkowników będących studentami studiów doktoranckich. Użytkownik otrzymuje informację z danymi kontaktowymi do pracownika, z którym powinien się kontaktować, ponieważ obecnie za te studia odpowiedzialna jest tylko jedna osoba, więc zbieranie kolejnych informacji jest zbędne.

7. Dialog **Prodziekan-dialog**

   Dialog uruchamiany po wybraniu opcji "Konsultacje z prodziekanem ds. studiów". Użytkownik w tym dialogu otrzymuje najpierw pytanie w elemencie **Prompt with multi-choice** o posiadanie lub brak statusu studenta. Jeśli użytkownik posiada status, zwracana jest odpowiedź z informacją, jak może się zarejestrować na konsultacje za pośrednictwem systemu ISOD, jeśli nie posiada statusu studenta, w serii pytań z wykorzystaniem elementów **Prompt for text** oraz **Prompt for a number** musi podać swoje imię i nazwisko, adres e-mail oraz nr albumu. Na podstawie tych informacji użytkownik jest zapisywany na konsultacje przez pracownika dziekanatu.

8. Dialog **Wniosek-dialog**

   Dialog uruchamiany po wybraniu opcji "Chcę złożyć wniosek". Użytkownik otrzymuje nazwy możliwych do złożenia wniosków w postaci listy(**Prompt with multi-choice**), z której musi wybrać jeden(np. podając jego liczbę). Następnie otrzymuje pytanie o posiadanie lub brak statusu studenta; jeśli posiada status, to dostaje informację o tym, jak można złożyć wniosek za pośrednictwem systemu ISOD, jeśli nie posiada statusu studenta; dostaje informację o tym, skąd może pobrać dany wniosek i jak może go złożyć w inny sposób.

9. Dialog **Start**

   Dialog uruchamiany na samym początku, po wpisaniu przez użytkownika frazy "start" za pomocą triggera o nazwie **start**. Dialog uruchamia przepływ.

10. Dialog **Pomoc**

    Dialog uruchamiany po wpisaniu przez użytkownika frazy "pomoc" za pomocą triggera o nazwie **pomoc**. Zwraca informację o podążaniu za sugerowanymi odpowiedziami, by uniknąć problemów, oraz o możliwości rozpoczęcia interakcji od początku po wpisaniu frazy "anuluj"

11. Dialog **Anuluj**

    Dialog uruchamiany po wpisaniu przez użytkownika frazy "anuluj" za pomocą triggera o nazwie **anuluj**. Kasuje podane do tej pory przez użytkownika dane oraz przenosi go do dialogu **Start** by móc rozpocząć interakcję jeszcze raz.

