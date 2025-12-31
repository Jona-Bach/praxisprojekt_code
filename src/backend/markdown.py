
def markdown_setup():
    md = """ # 🚀 Setup Guide

    Willkommen zur **FinSight** – Ihrem Tool für den Vergleich traditioneller Regressionsverfahren mit LLM-basierten Vorhersagemodellen für Finanzdaten.

    ---

    ## 📊 **Data**

    Die Data-Seite ist Ihr Ausgangspunkt für Aktienanalysen und Datenmanagement.

    ### **Single Stock Analysis**
    Analysieren Sie einzelne Aktien im Detail:
    - Aktuelle Kennzahlen und Fundamentaldaten
    - Preisentwicklung mit interaktiven Charts
    - Historische Performance-Metriken

    ### **Compared Stock Analysis**
    Vergleichen Sie zwei Aktien direkt miteinander, um relative Performance und Korrelationen zu identifizieren.

    ### **Sidebar-Funktionen**

    #### 🔄 **Update All Data**
    Lädt automatisch die neuesten Informationen für alle als "Initial" markierten Aktien herunter.

    #### 📦 **Update Processed Data**
    Überführt Kennzahlen manuell in die aufbereitete Datenbank (nur notwendig, falls die automatische Verarbeitung fehlschlägt).

    #### 🎯 **Update Single Ticker Data**
    Aktualisieren Sie gezielt einzelne Ticker aus Ihrer bestehenden Liste. *Hinweis: Prüfen Sie das Datum des letzten Updates, um den Datenstand zu kennen.*

    #### 📥 **Download Ticker Data**
    Suchen und laden Sie neue Aktien in Ihre Datenbank.

    **⚠️ Wichtig:** Für alle Download-Funktionen benötigen Sie einen **Alpha Vantage API Key**, der unter **Settings → Global Settings** hinterlegt werden muss (wird nur für die aktuelle Session gespeichert).

    ### **Create Your Own Database**
    Erstellen Sie benutzerdefinierte Datenbanken aus Excel- oder CSV-Dateien:
    - Vergeben Sie individuelle Datenbanknamen
    - Wählen Sie Funktionen wie "Replace" zum Überschreiben bestehender Datenbanken
    - Verwalten Sie erstellte Datenbanken unter **Settings → Data Settings**

    ---

    ## 🤖 **Machine Learning**

    ### **ML Studio**
    Bauen Sie eigene Machine Learning Modelle mit folgenden Optionen:

    **Konfiguration:**
    - Auswahl der Feature-Spalten
    - Definition der Zielvariable (Target)
    - Wahl des Algorithmus
    - Zeitreihen-Analyse aktivieren (optional)
    - Daten-Skalierung vorab durchführen (optional)

    **Verfügbare Algorithmen:**
    - Lineare Regression
    - Decision Tree
    - Random Forest
    - Logistische Regression (Klassifikation)
    - Binäre Klassifikation (z.B. Preis steigt/fällt)

    ⚠️ **Hinweis:** Das Programm führt Algorithmen ohne Validierung durch. Die Auswahl eines sinnvollen Algorithmus für Ihre Daten liegt in Ihrer Verantwortung!

    ### **Modell-Management**
    Im rechten Bereich können Sie:
    - Gespeicherte Modelle anzeigen
    - Modelle herunterladen
    - Modelle mit neuen Daten testen

    ---

    ## 🧠 **LLM Playground**

    Nutzen Sie die Kraft von Large Language Models für Finanzprognosen:

    **Konfiguration:**
    - Auswahl relevanter Datenspalten
    - Entwicklung eigener Prompts für das LLM
    - Wahl des Vorhersageverfahrens
    - Ollama-Backend auswählen:
    - Docker-internes Ollama (Standard)
    - Lokales Ollama
    - Container-basiertes lokales Ollama

    💡 **Empfehlung:** Verwenden Sie mathematisch spezialisierte Modelle wie **MathStral 7B** für optimale Ergebnisse bei finanziellen Berechnungen. Mit besseren Ressourcen und größeren Modellen steigen Qualität und Genauigkeit der Vorhersagen signifikant.

    ---

    ## 💬 **Assistant**

    Ein integrierter KI-Assistent steht Ihnen zur Verfügung, um die Navigation und Nutzung der Plattform zu erleichtern.

    **Konfiguration:** Passen Sie unter **Settings** das Modell und die Ollama-Quelle (lokal/Container) für den Assistenten an.

    ---

    ## ⚙️ **Settings**

    ### **Global Settings**
    - **Alpha Vantage API Key:** Erforderlich für Daten-Downloads (nur Session-Speicherung)
    - **Ollama-Modus:** Wählen Sie zwischen lokaler Installation und Docker-Container

    ### **Data Settings**
    - **Initiale Ticker-Liste:** Definieren Sie, welche Aktien standardmäßig geladen werden
    - **Analyse-Zeitraum:** Legen Sie fest, wie weit in die Vergangenheit Daten geladen werden
    - **Tabellen löschen:** Entfernen Sie nicht mehr benötigte Datenbanken

    ### **ML Settings**
    - **Minimale Zeilenanzahl:** Mindestgröße einer Tabelle für das Training
    - **Maximale Zeilenanzahl:** Obergrenze zur Ressourcenschonung

    ### **Assistenten-Einstellungen**
    - Modellauswahl für den KI-Assistenten
    - Ollama-Backend-Konfiguration

    ---

    ## 🎯 **Best Practices**

    1. **API Key sicher verwenden:** Der Alpha Vantage Key wird nur temporär gespeichert
    2. **Datenstand prüfen:** Kontrollieren Sie regelmäßig die Update-Timestamps Ihrer Ticker
    3. **Modellwahl:** Größere, spezialisierte Modelle liefern bessere Ergebnisse
    4. **Ressourcen:** Nutzen Sie die Zeilenbegrenzungen im ML Studio zur Optimierung
    5. **Eigene Datenbanken:** Testen Sie verschiedene Datenkombinationen für individualisierte Analysen

    ---

    ## 🔧 **Technische Hinweise**

    - Alle LLM-Funktionen verwenden **Ollama** als Backend
    - Bei Verwendung ohne Docker wählen Sie "Lokal" in den Einstellungen
    - Für externe Ollama-Instanzen nutzen Sie die IP-basierte Konfiguration
    - Die Plattform führt Berechnungen ohne Logikprüfung aus – Methodenwahl liegt beim Nutzer

    ---

    ## 📚 **Workflow-Empfehlung**

    1. **Einrichtung:** API Key hinterlegen, initiale Ticker-Liste erstellen
    2. **Daten laden:** Update All Data ausführen
    3. **Exploration:** Single Stock Analysis zur Datenprüfung
    4. **Modellierung:** ML Studio oder LLM Playground für Experimente
    5. **Vergleich:** Traditionelle ML vs. LLM-Ansätze evaluieren

    ---

    **Viel Erfolg bei Ihren Finanzanalysen! 📈**"""
    return md

def markdown_welcome():

    md = """## Welcome to FinSight 👋

FinSight helps you analyze stocks and compare **traditional regression-based models** with **LLM-powered forecasting**, all in one dashboard. Use it to explore market data, manage your ticker database, and test different prediction approaches on financial time series.

### What you can do here

- **Stock Data & Analysis**
  - Review key metrics, fundamentals, interactive price charts, and historical performance.
  - Compare two stocks side-by-side to understand relative performance and correlation.
  - Keep your dataset up to date (bulk updates or individual tickers) and download new tickers into your database.

- **Build Your Own Database**
  - Import Excel/CSV files to create custom datasets.
  - Choose whether to replace existing databases and manage them in **Settings → Data Settings**.

- **Machine Learning Studio**
  - Train baseline models by selecting features, defining a target, choosing an algorithm, and optionally enabling time-series mode or scaling.
  - Manage saved models, download them, and test them on new data.

- **LLM Playground**
  - Create prompt-driven forecasts using selected data columns and different prediction strategies.
  - Run LLMs via Ollama (Docker-internal, local, or container-based local backends).

- **Built-in Assistant**
  - Use the integrated AI assistant to help with navigation and getting things done faster inside the platform.
  - Configure the assistant’s model and Ollama source in **Settings** (local vs. container).

> **Note:** Some Functions may require an **Alpha Vantage API key** set in **Settings → Global Settings** (stored only for the current session)."""
    return md