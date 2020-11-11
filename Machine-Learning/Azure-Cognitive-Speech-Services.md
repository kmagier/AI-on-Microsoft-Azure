### Azure Cognitive Speech Services

#### 1. Przedstawienie usług

Usługi Azure Cognitive Speech Services są częścią ogólnej grupy usług Azure Cognitive Services; ich zadaniem jest zapewnienie przetwarzania mowy na tekst, tekstu na mowę oraz tłumaczenia tekstów z jednego języka na inny, z wykorzystaniem AI oraz Machine Learningu.

Najczęstsze zastosowania usługi:

* Tłumaczenie prezentacji na żywo
* Tłumaczenie osobistych lub zdalnych rozmów
* Wsparcie klienta
* Napisy do filmów/utworów muzycznych itd.

##### 1.1. Speech-to-text

Usługa speech-to-text pozwala na transkrypcję w czasie rzeczywistym plików dźwiękowych zawierających mowę, na tekst. Firma Microsoft wykorzystuje tą samą technologię rozpoznawania mowy w Cortanie i produktach Office. Usługę można łatwo łączyć z usługami translacji oraz text-to-speech.

Standardowo usługa speech-to-text wykorzystuje uniwersalny model językowy, który został wytrenowany z użyciem danych posiadanych przez firmę Microsoft. Możliwe jest jednak stworzenie i wytrenowanie swoich własnych modeli akustycznych, językowych oraz wymowy.

Przy dodaniu tekstu referencyjnego do pliku dźwiękowego zawierającego mowę, usługa speech-to-text posiada opcję oceny wymowy; potrafi określić dokładność oraz stopień płynności w posługiwaniu się językiem, na podstawie pliku dźwiękowego. Dzięki czemu np. osoby uczące się języka mogą ćwiczyć wymowę i bardzo szybko otrzymywać informację zwrotną, czy odpowiednio wypowiadają określone frazy. 

##### 1.2. Text-to-speech

Usługa text-to-speech umożliwia zamianę tekstu na syntezowaną mowę podobną do mowy ludzkiej. Umożliwia wybranie standardowych głosów, lub stworzeniu własnego. Usługa oferuje ponad 75 standardowych typów głosu oraz 5 głosów stworzonych z wykorzystaniem sieci neuronowych, dostępnych w 45 różnych językach i dialektach.

##### 1.3. Translacja mowy

Usługa translacji mowy umożliwia wielojęzykową translację mowy na mowę, mowy na tekst lub tekstu na mowę, w czasie rzeczywistym. Silnik translacyjny wykorzystuje dwa różne podejścia: statystyczną maszynę translacyjną i neuronową maszynę translacyjną.

Statystyczna maszyna translacyjna wykorzystuje zaawansowaną analizę statystyczną do oszacowania najlepszego możliwego dopasowania tłumaczenia biorąc pod uwage kontekst złożony z kilku słów.

Neuronowa maszyna translacyjna jest wykorzystywana do zapewnienia większej dokładności, oraz naturalnego brzmienia tekstu tłumaczenia, poprzez analizę pełnego kontekstu.

#### 2. Przykłady użycia

Przykładowe przypadki użycia(Speech-to-text):

* Zamiana mowy na tekst wiadomości w aplikacjach dla osób z niepełnosprawnością wzroku
* Wyodrębnienie z utworów muzycznych tekstów utworów
* W aplikacjach inteligentnego budynku do sterowania urządzeniami(zapalanie/gaszenie świateł, uruchamianie klimatyzacji, podnoszenie/opuszczanie rolet itd.)
* Zamiana dialogów w filmach na napisy do filmu dla osób słabo słyszących

Przykładowe przypadki użycia(Text-to-speech):

* Syntezatory mowy dla osób niemych
* Aplikacje do nauki wymowy zamieniające tekst w danym języku na poprawną wymowę podanego słowa lub frazy
* Do tworzenia prostych audiobooków na podstawie tekstu książki

Przykładowe przypadki użycia(Translacja):

* Tłumaczenie książek na wiele języków
* Tłumaczenie tekstów utworów muzycznych
* W aplikacjach typu chat, do tłumaczenia wiadomości użytkowników na zdefiniowany przez nich język

#### 3.How to

##### 3.1. SDK

Wszystkie typy usługi Cognitive Speech Services udostępniają SDK(Software Development Kit) w wielu językach programowania(m.in. Python, Java oraz C#). Oznacza to, że po ściągnięciu odpowiedniej biblioteki możemy korzystać ze wszystkich usług pisząc kod źródłowy aplikacji. Jedynym dodatkowym wymaganiem jest posiadanie aktywnego konta Azure, oraz utworzenie na swoim koncie usługi typu Azure Cognitive Speech Service; następnie korzystając z jej klucza, możemy za pośrednictwem naszych programów łączyć się z usługą Azure Cognitive Speech Services i korzystać ze wspomnianych wcześniej usług.

##### 3.2. Interfejs REST API

Usługi Azure Cognitive Speech Services posiadają dostępny interfejs typu REST API, dzięki czemu możemy korzystać z nich również wysyłając zapytania metody POST. Do tego potrzebny jest również klucz API, oraz zapytanie wysłane pod interfejs REST API zawierający odpowiednie nagłówki, opisane w dokumentacji usługi na portalu Microsoft.

#### 4. Pricing

Usługa dostępna jest w dwóch wariantach: **Free** oraz **Standard**, które różnią się ilością obsługiwanych jednocześnie zapytań:

W wariancie **Free** - Aplikacja Web/Kontener obsługują 1 zapytanie

W wariancie **Standard** - Aplikacja Web/Kontener obsługują 20 zapytań

Specyfikacja konkretnej usługi dla konkretnego wariantu jest bardzo rozbudowana, dlatego, że wyróżnione są 4 główne usługi: Speech to Text, Text to Speech, Speech Translation oraz Speaker Recognition, z których każda posiada kilka wariantów zastosowania, by dowiedzieć się ile kosztuje konkretna usługa należy odwiedzić stronę platformy Azure poświęconą usługach Azure Cognitive Speech: [Azure Cognitive Speech Services - cennik](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/).



