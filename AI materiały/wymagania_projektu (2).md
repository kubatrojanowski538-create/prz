# Wymagania projektu

## 1. Zakres projektu

Celem projektu jest przygotowanie kompletnego rozwiązania do klasyfikacji próbek tkanki piersi na podstawie danych liczbowych pochodzących ze spektroskopii impedancji elektrycznej. Projekt powinien obejmować pełny proces: przygotowanie danych, analizę eksploracyjną, implementację wybranego modelu ML, ocenę modelu, optymalizację konfiguracji oraz opracowanie wyników w formie raportu.

Wymagania nie narzucają konkretnego algorytmu ML ani konkretnej listy testowanych hiperparametrów. Model powinien być opisany ogólnie jako **wybrany model ML**.

## 2. Ogólny opis gry

Projekt jest zbudowany wokół gry napisanej w języku C++, przedstawiającej jazdę samochodem w środowisku 2D. Gracz lub algorytm steruje pojazdem poruszającym się po planszy albo trasie, a stan gry może obejmować między innymi pozycję, kierunek, prędkość oraz informacje o najbliższym otoczeniu. Gra pełni rolę środowiska, w którym można zbierać dane, testować zachowanie wybranego modelu ML lub wykorzystywać predykcje modelu do podejmowania decyzji sterujących.

Opis gry ma charakter ogólny i nie definiuje szczegółowej mechaniki rozgrywki, zasad punktacji, wyglądu planszy ani konkretnego sposobu implementacji fizyki pojazdu.

## 3. Wymagania dotyczące danych

### WD-01. Źródło danych
Projekt powinien korzystać ze zbioru Breast Tissue zawierającego próbki tkanki piersi opisane cechami numerycznymi.

### WD-02. Charakter problemu
System powinien rozwiązywać problem klasyfikacji wieloklasowej, w którym każda próbka jest przypisywana do jednej z dostępnych klas tkanki.

### WD-03. Cechy wejściowe
Dane wejściowe powinny obejmować cechy liczbowe opisujące właściwości impedancyjne próbek.

### WD-04. Etykieta wyjściowa
Zmienna wyjściowa powinna reprezentować klasę tkanki przypisaną do danej próbki.

### WD-05. Obsługa danych surowych
Projekt powinien umożliwiać wczytanie danych z pliku źródłowego, np. arkusza Excel, oraz przekształcenie ich do formatu używanego przez skrypty eksperymentalne.

### WD-06. Usunięcie kolumn technicznych
Z danych należy usunąć kolumny porządkowe lub identyfikacyjne, które nie niosą informacji diagnostycznej i nie powinny być używane jako cechy modelu.

### WD-07. Podział na cechy i etykiety
Skrypt przygotowujący dane powinien rozdzielać zbiór na macierz cech `X` oraz wektor etykiet `y`.

### WD-08. Kodowanie etykiet
Tekstowe etykiety klas powinny zostać zakodowane do postaci liczbowej, przy jednoczesnym zachowaniu mapowania na oryginalne nazwy klas.

### WD-09. Normalizacja danych
Projekt powinien przewidywać możliwość normalizacji cech, tak aby przygotowany zbiór mógł być użyty również z modelami wrażliwymi na skalę danych.

### WD-10. Zapis przygotowanego zbioru
Przetworzone dane powinny zostać zapisane do pliku pośredniego, np. `breast_tissue.npz`, zawierającego co najmniej cechy, etykiety, nazwy cech i nazwy klas.

## 4. Wymagania dotyczące analizy eksploracyjnej

### WA-01. Statystyki opisowe
Projekt powinien generować podstawowe statystyki opisowe cech, w szczególności średnią, odchylenie standardowe, minimum i maksimum.

### WA-02. Analiza rozkładu klas
Projekt powinien sprawdzać liczebność poszczególnych klas oraz generować wykres rozkładu klas.

### WA-03. Ocena zbalansowania klas
W raporcie należy odnieść się do stopnia zbalansowania klas i wpływu tego faktu na wybór metryk oceny.

### WA-04. Analiza zależności między cechami
Projekt powinien generować macierz korelacji cech oraz zawierać krótki opis najważniejszych obserwacji wynikających z tej analizy.

### WA-05. Wizualizacje EDA
Wykresy analizy eksploracyjnej powinny być zapisywane do plików, aby można było wykorzystać je w raporcie.

## 5. Wymagania dotyczące modelu ML

### WM-01. Implementacja klasyfikatora
Projekt powinien implementować wybrany model ML przeznaczony do klasyfikacji wieloklasowej.

### WM-02. Model bazowy
Należy wyznaczyć wynik modelu bazowego, który będzie punktem odniesienia dla dalszej optymalizacji.

### WM-03. Strojenie konfiguracji
Projekt powinien przeprowadzać optymalizację konfiguracji wybranego modelu ML bez narzucania w wymaganiach konkretnej listy parametrów.

### WM-04. Analiza wpływu konfiguracji
Należy zbadać wpływ zmian konfiguracji modelu na jakość klasyfikacji, przedstawiając wyniki w formie tabel i/lub wykresów.

### WM-05. Globalna optymalizacja
Projekt powinien obejmować etap globalnego przeszukiwania zdefiniowanej przestrzeni konfiguracji modelu.

### WM-06. Wybór najlepszego modelu
Na podstawie wyników walidacji należy wybrać najlepszą znalezioną konfigurację wybranego modelu ML.

### WM-07. Końcowe uczenie modelu
Najlepszy model powinien zostać wytrenowany i oceniony w końcowym etapie eksperymentu.

## 6. Wymagania dotyczące metodyki eksperymentów

### WE-01. Powtarzalność eksperymentów
Eksperymenty powinny być powtarzalne dzięki zastosowaniu stałego ziarna losowości tam, gdzie jest to wymagane.

### WE-02. Walidacja krzyżowa
Ocena jakości modelu powinna wykorzystywać stratyfikowaną walidację krzyżową, aby zachować proporcje klas w kolejnych podziałach.

### WE-03. Metryka główna
Główną metryką jakości powinna być poprawność klasyfikacji wyrażona procentowo.

### WE-04. Metryki uzupełniające
Końcowa ewaluacja powinna obejmować dodatkowe metryki klasyfikacji, takie jak precyzja, czułość i F1-score dla poszczególnych klas.

### WE-05. Oddzielny zbiór testowy
Projekt powinien przewidywać końcową ocenę najlepszego modelu na wydzielonym zbiorze testowym z zachowaniem stratyfikacji.

### WE-06. Porównanie z modelem bazowym
Wyniki najlepszego modelu powinny zostać porównane z wynikiem modelu bazowego.

### WE-07. Analiza błędów
Projekt powinien zawierać analizę błędnych klasyfikacji, najlepiej z wykorzystaniem macierzy pomyłek.

## 7. Wymagania dotyczące wyników i raportowania

### WR-01. Zapis wykresów
Wszystkie istotne wykresy powinny być zapisywane do plików graficznych.

### WR-02. Zapis tabel
Tabele z wynikami powinny być zapisywane do plików tekstowych lub formatu możliwego do włączenia do raportu.

### WR-03. Podsumowanie wyników
Projekt powinien tworzyć zbiorcze podsumowanie najważniejszych wyników, np. w pliku JSON.

### WR-04. Raport końcowy
Raport powinien zawierać opis celu projektu, podstawy teoretyczne, analizę danych, metodykę eksperymentów, wyniki, porównanie modeli oraz wnioski.

### WR-05. Wizualizacja końcowej oceny
Raport powinien zawierać co najmniej macierz pomyłek oraz raport klasyfikacji najlepszego modelu.

### WR-06. Interpretacja modelu
Jeżeli wybrany model ML to umożliwia, projekt powinien zawierać analizę istotności cech lub inną formę interpretacji decyzji modelu.

### WR-07. Wnioski
W raporcie należy wskazać najważniejsze obserwacje dotyczące jakości klasyfikacji, trudności problemu, klas najczęściej mylonych oraz możliwych kierunków dalszych prac.

## 8. Wymagania dotyczące struktury projektu

### WS-01. Skrypt przygotowania danych
Projekt powinien zawierać osobny skrypt odpowiedzialny za wczytanie, oczyszczenie, zakodowanie i zapis przygotowanego zbioru.

### WS-02. Skrypt eksperymentalny
Projekt powinien zawierać główny skrypt uruchamiający analizę eksploracyjną, trenowanie, walidację, optymalizację i końcową ewaluację modelu.

### WS-03. Katalog danych
Dane surowe i przygotowane powinny być przechowywane w wydzielonym katalogu, np. `dane/`.

### WS-04. Katalog wyników
Wykresy, tabele i podsumowania powinny być zapisywane w wydzielonym katalogu wynikowym, np. `wyniki/`.

### WS-05. Katalog materiałów do raportu
Elementy przeznaczone do raportu mogą być dodatkowo kopiowane do osobnych katalogów, np. `latex/rysunki/` i `latex/tabele/`.

### WS-06. Automatyzacja
Po uruchomieniu skryptów projekt powinien samodzielnie odtworzyć pełny przebieg eksperymentu od przygotowania danych do zapisania wyników.

## 9. Wymagania technologiczne

### WT-01. Język programowania
Projekt powinien być wykonany w języku Python.

### WT-02. Biblioteki do przetwarzania danych
Projekt powinien wykorzystywać biblioteki umożliwiające wczytywanie i przetwarzanie danych tabelarycznych oraz operacje numeryczne, np. `pandas` i `numpy`.

### WT-03. Biblioteki ML
Projekt powinien wykorzystywać bibliotekę umożliwiającą implementację, walidację i optymalizację modeli uczenia maszynowego, np. `scikit-learn`.

### WT-04. Biblioteki wizualizacyjne
Projekt powinien wykorzystywać biblioteki do tworzenia wykresów, np. `matplotlib` i `seaborn`.

### WT-05. Tryb bez okna graficznego
Generowanie wykresów powinno działać w trybie zapisu do plików, bez konieczności ręcznego otwierania okien graficznych.

## 10. Kryteria akceptacji

### KA-01. Przygotowanie danych
Po uruchomieniu skryptu przygotowania danych powstaje plik z gotowymi tablicami cech, etykiet, nazw cech i nazw klas.

### KA-02. Analiza EDA
Po uruchomieniu głównego skryptu powstają wykresy rozkładu klas i korelacji cech oraz tabela statystyk opisowych.

### KA-03. Walidacja modelu
Główny skrypt wyznacza wynik modelu bazowego oraz wynik najlepszego znalezionego modelu w walidacji krzyżowej.

### KA-04. Optymalizacja
Projekt wykonuje strojenie konfiguracji wybranego modelu ML i zapisuje wyniki tego procesu.

### KA-05. Końcowa ewaluacja
Projekt generuje końcową ocenę najlepszego modelu, w tym macierz pomyłek i raport klasyfikacji.

### KA-06. Powtarzalność
Ponowne uruchomienie projektu na tych samych danych i ustawieniach powinno prowadzić do odtworzenia tych samych wyników lub wyników zgodnych z przyjętą metodyką.

### KA-07. Kompletność raportu
Raport końcowy zawiera opis celu, danych, przygotowania danych, metodyki, wyników, ewaluacji oraz wniosków.

## 11. Zakres wyłączony

- Wymagania nie definiują konkretnego algorytmu ML.
- Wymagania nie zawierają konkretnej listy testowanych hiperparametrów.
- Wymagania nie narzucają jednej konkretnej końcowej konfiguracji modelu.
- Wymagania nie zakładają, że normalizacja jest obowiązkowa dla każdego typu modelu, ale powinna być dostępna jako element przygotowania danych.
