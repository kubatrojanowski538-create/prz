#!/usr/bin/env python3
"""Generate diagrams for lab exercise 6.

The lab handout asks for FHD diagrams in UMLet and DFD diagrams in Oracle SQL
Developer Data Modeler. Those GUI tools are not available in this cloud
environment, so this script renders equivalent editable sources with Graphviz.
The shapes follow the notation from the theory material: process, flow, data
store and external actor.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def render(name: str, dot: str) -> None:
    """Write DOT source and render SVG/PNG variants."""
    dot_path = BASE_DIR / f"{name}.dot"
    dot_path.write_text(dot.strip() + "\n", encoding="utf-8")

    for fmt in ("svg", "png"):
        subprocess.run(
            ["dot", f"-T{fmt}", str(dot_path), "-o", str(BASE_DIR / f"{name}.{fmt}")],
            check=True,
        )


def fhd_diagram(name: str, title: str, edges: list[tuple[str, str]], labels: dict[str, str]) -> None:
    nodes = "\n".join(
        f'  "{node}" [label="{label}"];' for node, label in labels.items()
    )
    edge_lines = "\n".join(f'  "{src}" -> "{dst}";' for src, dst in edges)
    render(
        name,
        f"""
digraph G {{
  graph [
    rankdir=TB,
    splines=ortho,
    nodesep=0.55,
    ranksep=0.75,
    bgcolor="white",
    labelloc="t",
    label="{title}",
    fontname="Arial",
    fontsize=20
  ];
  node [
    shape=box,
    style="rounded,filled",
    fillcolor="#f8fbff",
    color="#3b6ea8",
    penwidth=1.4,
    fontname="Arial",
    fontsize=12,
    margin="0.14,0.08"
  ];
  edge [
    color="#3b6ea8",
    arrowsize=0.6,
    arrowhead=none,
    penwidth=1.2
  ];

{nodes}
{edge_lines}
}}
""",
    )


def dfd_common_header(title: str, rankdir: str = "LR") -> str:
    return f"""
digraph G {{
  graph [
    rankdir={rankdir},
    splines=true,
    nodesep=0.55,
    ranksep=0.75,
    bgcolor="white",
    labelloc="t",
    label="{title}",
    fontname="Arial",
    fontsize=20,
    compound=true
  ];
  node [fontname="Arial", fontsize=11, margin="0.12,0.08"];
  edge [fontname="Arial", fontsize=9, color="#3f3f3f", arrowsize=0.7];

  node [shape=box, style="rounded,filled", fillcolor="#fff2cc", color="#b57f00", penwidth=1.3];
"""


def actor(node: str, label: str) -> str:
    return f'  {node} [label="{label}"];\n'


def process_block(items: list[tuple[str, str]]) -> str:
    lines = ['  node [shape=ellipse, style="filled", fillcolor="#dae8fc", color="#2f5597", penwidth=1.4];']
    lines += [f'  {node} [label="{label}"];' for node, label in items]
    return "\n".join(lines) + "\n"


def store_block(items: list[tuple[str, str]]) -> str:
    lines = ['  node [shape=cylinder, style="filled", fillcolor="#e2f0d9", color="#548235", penwidth=1.3];']
    lines += [f'  {node} [label="{label}"];' for node, label in items]
    return "\n".join(lines) + "\n"


def flow(src: str, dst: str, label: str) -> str:
    return f'  {src} -> {dst} [label="{label}"];\n'


def build_diagrams() -> None:
    fhd_diagram(
        "fhd_01_glowne_funkcje",
        "FHD - System obsługi zamówień: funkcje główne",
        [
            ("root", "f1"),
            ("root", "f2"),
            ("root", "f3"),
            ("root", "f4"),
            ("root", "f5"),
        ],
        {
            "root": "0. System obsługi zamówień",
            "f1": "1. Obsługa zamówień",
            "f2": "2. Obsługa klientów",
            "f3": "3. Obsługa rejonów",
            "f4": "4. Obsługa wyrobów",
            "f5": "5. Obsługa magazynu",
        },
    )

    fhd_diagram(
        "fhd_02_dekompozycja_magazyn_rejon_klient",
        "FHD - Dekompozycja funkcji: Klient, Rejon, Magazyn",
        [
            ("root", "f1"),
            ("root", "f2"),
            ("root", "f3"),
            ("root", "f4"),
            ("root", "f5"),
            ("f2", "f21"),
            ("f2", "f22"),
            ("f2", "f23"),
            ("f2", "f24"),
            ("f2", "f25"),
            ("f3", "f31"),
            ("f3", "f32"),
            ("f3", "f33"),
            ("f3", "f34"),
            ("f3", "f35"),
            ("f5", "f51"),
            ("f5", "f52"),
            ("f5", "f53"),
            ("f5", "f54"),
            ("f5", "f55"),
        ],
        {
            "root": "0. System obsługi zamówień",
            "f1": "1. Obsługa zamówień\\n(...)",
            "f2": "2. Obsługa klientów",
            "f3": "3. Obsługa rejonów",
            "f4": "4. Obsługa wyrobów\\n(...)",
            "f5": "5. Obsługa magazynu",
            "f21": "2.1 Rejestracja klienta",
            "f22": "2.2 Aktualizacja danych klienta",
            "f23": "2.3 Przypisanie klienta do rejonu",
            "f24": "2.4 Weryfikacja statusu klienta",
            "f25": "2.5 Udostępnienie historii zamówień",
            "f31": "3.1 Definiowanie rejonu",
            "f32": "3.2 Przypisanie klientów do rejonu",
            "f33": "3.3 Przypisanie magazynu obsługującego",
            "f34": "3.4 Analiza zapotrzebowania rejonu",
            "f35": "3.5 Raportowanie rejonowe",
            "f51": "5.1 Przyjęcie wyrobów",
            "f52": "5.2 Ewidencja stanów magazynowych",
            "f53": "5.3 Rezerwacja wyrobów pod zamówienie",
            "f54": "5.4 Kompletacja i wydanie zamówienia",
            "f55": "5.5 Uzupełnianie zapasów",
        },
    )

    context = dfd_common_header("DFD - Diagram kontekstowy systemu obsługi zamówień")
    context += actor("klient", "Klient")
    context += actor("pracownik", "Pracownik obsługi")
    context += actor("magazynier", "Magazynier")
    context += actor("kierownik", "Kierownik sprzedaży")
    context += process_block([("system", "0\\nSystem obsługi\\nzamówień")])
    context += flow("klient", "system", "dane klienta, zamówienie")
    context += flow("system", "klient", "potwierdzenie, status realizacji")
    context += flow("pracownik", "system", "dyspozycje obsługi, korekty danych")
    context += flow("system", "pracownik", "informacje o zamówieniach i klientach")
    context += flow("magazynier", "system", "stany, potwierdzenia wydań")
    context += flow("system", "magazynier", "dyspozycje rezerwacji i kompletacji")
    context += flow("kierownik", "system", "parametry rejonów, zapytania raportowe")
    context += flow("system", "kierownik", "raporty rejonów, sprzedaży i zapasów")
    context += "}\n"
    render("dfd_01_kontekstowy", context)

    system = dfd_common_header("DFD - Diagram systemowy: główne funkcje")
    system += actor("klient", "Klient")
    system += actor("pracownik", "Pracownik obsługi")
    system += actor("magazynier", "Magazynier")
    system += actor("kierownik", "Kierownik sprzedaży")
    system += process_block(
        [
            ("p1", "1.0\\nObsługa zamówień"),
            ("p2", "2.0\\nObsługa klientów"),
            ("p3", "3.0\\nObsługa rejonów"),
            ("p4", "4.0\\nObsługa wyrobów"),
            ("p5", "5.0\\nObsługa magazynu"),
        ]
    )
    system += store_block(
        [
            ("d1", "D1\\nZamówienia"),
            ("d2", "D2\\nKlienci"),
            ("d3", "D3\\nRejony"),
            ("d4", "D4\\nWyroby"),
            ("d5", "D5\\nStany magazynowe"),
        ]
    )
    for src, dst, label in [
        ("klient", "p2", "dane rejestracyjne / aktualizacje"),
        ("p2", "d2", "dane klienta"),
        ("d2", "p2", "profil klienta"),
        ("p2", "p3", "adres i rejon klienta"),
        ("klient", "p1", "zamówienie"),
        ("p1", "d1", "nagłówek i pozycje zamówienia"),
        ("d1", "p1", "historia i status zamówień"),
        ("p1", "p4", "pozycje zamówienia"),
        ("p4", "d4", "katalog wyrobów"),
        ("d4", "p4", "dane wyrobów"),
        ("p1", "p5", "zapotrzebowanie / rezerwacja"),
        ("p5", "d5", "rezerwacje i aktualne stany"),
        ("d5", "p5", "dostępność wyrobów"),
        ("p5", "p1", "potwierdzenie kompletacji"),
        ("p1", "klient", "potwierdzenie i status"),
        ("pracownik", "p1", "korekta zamówienia"),
        ("pracownik", "p2", "obsługa klienta"),
        ("kierownik", "p3", "definicje rejonów"),
        ("p3", "d3", "dane rejonu"),
        ("d3", "p3", "struktura rejonów"),
        ("p3", "p5", "magazyn obsługujący rejon"),
        ("magazynier", "p5", "przyjęcia i wydania"),
        ("p5", "magazynier", "lista kompletacji"),
        ("p3", "kierownik", "raport rejonowy"),
    ]:
        system += flow(src, dst, label)
    system += "}\n"
    render("dfd_02_systemowy", system)

    klient = dfd_common_header("DFD szczegółowy - 2.0 Obsługa klientów")
    klient += actor("klient", "Klient")
    klient += actor("pracownik", "Pracownik obsługi")
    klient += process_block(
        [
            ("p21", "2.1\\nPrzyjęcie danych klienta"),
            ("p22", "2.2\\nWeryfikacja danych"),
            ("p23", "2.3\\nPrzypisanie do rejonu"),
            ("p24", "2.4\\nZapis / aktualizacja klienta"),
            ("p25", "2.5\\nUdostępnienie danych do zamówień"),
        ]
    )
    klient += store_block([("d2", "D2\\nKlienci"), ("d3", "D3\\nRejony"), ("d1", "D1\\nZamówienia")])
    for src, dst, label in [
        ("klient", "p21", "formularz danych"),
        ("pracownik", "p21", "dane z obsługi bezpośredniej"),
        ("p21", "p22", "dane klienta"),
        ("p22", "p23", "dane poprawne"),
        ("p22", "klient", "prośba o korektę"),
        ("d3", "p23", "lista rejonów"),
        ("p23", "p24", "klient + rejon"),
        ("p24", "d2", "rekord klienta"),
        ("d2", "p25", "dane klienta"),
        ("d1", "p25", "historia zamówień"),
        ("p25", "pracownik", "profil klienta"),
        ("p25", "klient", "potwierdzenie danych"),
    ]:
        klient += flow(src, dst, label)
    klient += "}\n"
    render("dfd_03_szczegolowy_klient", klient)

    rejon = dfd_common_header("DFD szczegółowy - 3.0 Obsługa rejonów")
    rejon += actor("kierownik", "Kierownik sprzedaży")
    rejon += actor("pracownik", "Pracownik obsługi")
    rejon += process_block(
        [
            ("p31", "3.1\\nDefiniowanie rejonu"),
            ("p32", "3.2\\nPrzypisanie klientów"),
            ("p33", "3.3\\nPrzypisanie magazynu"),
            ("p34", "3.4\\nAnaliza zapotrzebowania"),
            ("p35", "3.5\\nRaportowanie rejonowe"),
        ]
    )
    rejon += store_block(
        [
            ("d3", "D3\\nRejony"),
            ("d2", "D2\\nKlienci"),
            ("d1", "D1\\nZamówienia"),
            ("d5", "D5\\nStany magazynowe"),
        ]
    )
    for src, dst, label in [
        ("kierownik", "p31", "nazwa, zasięg, parametry rejonu"),
        ("p31", "d3", "dane rejonu"),
        ("pracownik", "p32", "adres klienta / korekta rejonu"),
        ("d2", "p32", "klienci"),
        ("d3", "p32", "aktywny rejon"),
        ("p32", "d2", "przypisanie rejonu klienta"),
        ("d3", "p33", "rejon"),
        ("d5", "p33", "magazyny i dostępność"),
        ("p33", "d3", "magazyn obsługujący"),
        ("d1", "p34", "zamówienia z rejonu"),
        ("d2", "p34", "klienci z rejonu"),
        ("p34", "p35", "agregaty zapotrzebowania"),
        ("d3", "p35", "definicje rejonów"),
        ("p35", "kierownik", "raport rejonowy"),
    ]:
        rejon += flow(src, dst, label)
    rejon += "}\n"
    render("dfd_04_szczegolowy_rejon", rejon)

    magazyn = dfd_common_header("DFD szczegółowy - 5.0 Obsługa magazynu")
    magazyn += actor("magazynier", "Magazynier")
    magazyn += actor("dostawca", "Dostawca")
    magazyn += actor("pracownik", "Pracownik obsługi")
    magazyn += process_block(
        [
            ("p51", "5.1\\nPrzyjęcie wyrobów"),
            ("p52", "5.2\\nAktualizacja stanów"),
            ("p53", "5.3\\nRezerwacja pod zamówienie"),
            ("p54", "5.4\\nKompletacja i wydanie"),
            ("p55", "5.5\\nUzupełnianie zapasów"),
        ]
    )
    magazyn += store_block(
        [
            ("d4", "D4\\nWyroby"),
            ("d5", "D5\\nStany magazynowe"),
            ("d1", "D1\\nZamówienia"),
        ]
    )
    for src, dst, label in [
        ("dostawca", "p51", "dostawa wyrobów"),
        ("magazynier", "p51", "potwierdzenie przyjęcia"),
        ("p51", "d4", "dane wyrobu"),
        ("p51", "p52", "przyjęta ilość"),
        ("p52", "d5", "aktualny stan"),
        ("d5", "p52", "stan przed zmianą"),
        ("pracownik", "p53", "dyspozycja rezerwacji"),
        ("d1", "p53", "pozycje zamówienia"),
        ("d5", "p53", "dostępność"),
        ("p53", "d5", "rezerwacja"),
        ("p53", "p54", "lista kompletacji"),
        ("magazynier", "p54", "potwierdzenie wydania"),
        ("p54", "d5", "rozchód magazynowy"),
        ("p54", "d1", "status kompletacji"),
        ("d5", "p55", "poziomy minimalne i braki"),
        ("p55", "dostawca", "zamówienie uzupełnienia"),
        ("p55", "pracownik", "informacja o brakach"),
    ]:
        magazyn += flow(src, dst, label)
    magazyn += "}\n"
    render("dfd_05_szczegolowy_magazyn", magazyn)

    readme = """# Ćwiczenie 6 - diagramy FHD i DFD

Wygenerowane diagramy dla systemu obsługi zamówień na podstawie instrukcji z `io-instrukcjeef.pdf` oraz materiałów teoretycznych o FHD/DFD.

## Pliki

- `fhd_01_glowne_funkcje.svg/png` - FHD z minimum pięcioma funkcjami głównymi.
- `fhd_02_dekompozycja_magazyn_rejon_klient.svg/png` - FHD z dekompozycją funkcji Klient, Rejon i Magazyn.
- `dfd_01_kontekstowy.svg/png` - DFD kontekstowy systemu obsługi zamówień.
- `dfd_02_systemowy.svg/png` - DFD systemowy dla funkcji głównych.
- `dfd_03_szczegolowy_klient.svg/png` - DFD szczegółowy procesu Obsługa klientów.
- `dfd_04_szczegolowy_rejon.svg/png` - DFD szczegółowy procesu Obsługa rejonów.
- `dfd_05_szczegolowy_magazyn.svg/png` - DFD szczegółowy procesu Obsługa magazynu.

Każdy diagram ma też edytowalne źródło `.dot`.
"""
    (BASE_DIR / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    build_diagrams()
