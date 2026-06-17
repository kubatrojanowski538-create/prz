# Projekt LaTeX — Nauczenie komputera sterowania samochodem w grze 2D

Raport końcowy projektu z uczenia maszynowego. Celem projektu jest **nauczenie
komputera sterowania samochodem w grze 2D** (sieć neuronowa jako kierowca), a nie
samo testowanie wartości hiperparametrów.

## Zawartość

- `main.tex` — plik źródłowy raportu (LaTeX),
- `rysunki/` — wykresy i ilustracje używane w raporcie (PNG),
- `main.pdf` — skompilowany raport (dla wygody),
- `.gitignore` — pomijane artefakty kompilacji.

## Kompilacja

Wymagana dystrybucja TeX (np. TeX Live) z obsługą języka polskiego
(`texlive-lang-polish`).

Najprościej za pomocą `latexmk`:

```bash
latexmk -pdf main.tex
```

Alternatywnie, dwukrotne uruchomienie `pdflatex` (aby zbudować spis treści):

```bash
pdflatex main.tex
pdflatex main.tex
```

Wynikiem jest plik `main.pdf`.

## Źródło materiałów

Raport powstał na podstawie materiałów z katalogu `AI materiały/`:
gra w C++ (raylib), skrypty uczące w Pythonie (PyTorch, scikit-learn),
zebrane dane (`GameStatesTable.csv`) oraz wykresy wyników.
