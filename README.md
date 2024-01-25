# Intelligenter_Reiseassistent

Der "Intelligenter_Reiseassistent" ist eine auf Flask basierende Webanwendung, die es Benutzern ermöglicht, Reisepläne und Routen basierend auf ihren Präferenzen zu erstellen. Das Projekt verwendet Machine Learning, um Bewertungen vorherzusagen, und Suchalgorithmen, um die optimale Reiseroute vorzuschlagen.

## Funktionen

- Eingabe der Benutzerpräferenzen erfolgt über eine JSON-Schnittstelle.
- Prognose von Benutzerpräferenzen mit einem ML-Modell (Random Forest Regression).
- Berechnung der optimalen Route durch den Best-First Search-Suchalgorithmus.
- Visualisierung der Reiseroute auf einer interaktiven Karte.

## Installation

Um das Projekt lokal zu installieren, folgen Sie diesen Schritten:

1. Klonen Sie das Repository:

   ```bash
   git clone https://github.com/Nabeelmeassar/Intelligenter_Reiseassistent.git
   ```

2. Installieren Sie die erforderlichen Abhängigkeiten:

   Stellen Sie sicher, dass Python 3.11 installiert ist, und führen Sie dann den folgenden Befehl aus:

   ```bash
   pip install -r requirements.txt
   ```

   Alternativ können Sie eine neue Python-Umgebung erstellen. Siehe Anhang Abbildung 6 für Anweisungen zur Erstellung einer Python-Umgebung.

## Verwendung

Nach dem Start der Anwendung können Sie Benutzerpräferenzen über die `/post_preference_json` Route senden, um eine personalisierte Reiseroute zu erhalten.

## Struktur

Das Projekt ist wie folgt strukturiert:

- `Intelligenter_Reiseassistent/`: Hauptverzeichnis des Flask-Projekts.
- `Classes/`: Enthält Klassen wie `TravelAssistant` und `TravelPlanner`.
- `static/csv/`: Beinhaltet CSV-Dateien mit Trainingsdaten für das ML-Modell.

## Mitwirken

Interessierte Mitwirkende sind willkommen und können gerne Pull Requests einreichen. Für größere Änderungen, bitte erst ein Issue erstellen, um darüber zu diskutieren.
