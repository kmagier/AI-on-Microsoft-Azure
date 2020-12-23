Ten folder zawiera prosty program napisany w Pythonie do testowania działania Custom Vision API.

## Projekt - System rozpoznawania rasy psa

##### 1. Use case

System realizuje problem rozpoznawania rasy psa na podstawie wgranego pliku graficznego.

Z systemu można skorzystać za pomocą platformy customvision.ai lub komunikując się z API usługi Custom Vision, za pomocą prostego programu znajdującego się w tym samym katalogu.

System zakłada dwa scenariusze:

1. Użytkownik wgrywa zdjęcie psa, którego rasę chciałby poznać, za pośrednictwem portalu customvision.ai; system zwraca informację o dopasowaniu w procentach(im więcej, tym większe dopasowanie zdjęcia do danej rasy)
2. Użytkownik korzysta z API usługi i podaje link do zdjęcia, w odpowiedzi API zwraca informację o dopasowaniach.

##### 2. Wykonanie

Do stworzenia systemu wykorzystano 10-12 zdjęć wybranych 14 ras psów. Zdjęcia zostały pobrane z serwisu Google grafika. Przy doborze zdjęć starano się wybrać jak najbardziej różniące się od siebie zdjęcia, uwzględniając również wiek psa oraz różnice w możliwych kolorach sierści danej rasy. Osobno wydzielono zbiór testowy składający się z 3-5 zdjęć, niewykorzystanych w procesie trenowania. Po wytrenowaniu modelu przetestowano działanie na zbiorze testowym. Dodatkowo napisano program w języku Python do sprawdzenia działania komunikacji z opublikowanym modelem za pośrednictwem API usługi Custom Vision. Program zwraca informację o 5 najwyższych dopasowaniach dla zdjęcia podanego w linku, lub informację o błędzie, jeśli nie programowi nie udało się z jakichś powodów połączyć z usługą.

##### 3. Pomysł na rozbudowę

Na podstawie przeprowadzonych testów, warto rozwinąć program testujący działanie komunikacji z API o frontend. Dobrym pomysłem mogłoby być stworzenie aplikacji korzystając z jakiegoś frameworka języka Python, np. z Flaska, zawierającej formularz, w którym użytkownik mógłby podać link do zdjęcia lub wgrać zdjęcie z dysku; po wykonaniu tego kroku, aplikacja łączyłaby się z API i pobierała informację o dopasowaniu, którą zwracałaby użytkownikowi w czytelnej formie.

